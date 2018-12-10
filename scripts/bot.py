import os
import json
import logging
import random
import re
from uuid import uuid4, UUID
from random import randint, choice
from time import sleep
from threading import Thread
from typing import Dict
from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities
from user_agent import generate_user_agent
from django.utils import timezone

from walker_panel.models import Task, Proxy, User, Log

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./logs/log')
logger = logging.getLogger('site_walker')
logger.setLevel(logging.INFO)

SCREENSHOTS_DIR = './screenshots/'
YANDEX_URL = 'http://yandex.ru'


def get_random_screen_resolution() -> str:
    resolutions = ['1280,768',
                   '1280,800',
                   '1280,1024',
                   '1360,768',
                   '1366,768',
                   '1440,900',
                   '1536,864',
                   '1600,900',
                   '1680,1050',
                   '1920,1080',
                   '1920,1200',
                   '2560,1080',
                   '2560,1440']

    return random.choice(resolutions)


def do_delay(delay: str = 'normal'):
    if delay == 'fast':
        sleep(randint(1, 5))
    elif delay == 'normal':
        sleep(randint(5, 15))
    elif delay == 'slow':
        sleep(randint(15, 30))
    else:
        sleep(randint(1, 30))


def generate_browser_configuration(task: Task) -> Dict[str, str]:
    config = {'user-agent': generate_user_agent(),
              'resolution': get_random_screen_resolution()}

    user_proxy_count = Proxy.objects.filter(owner=task.owner).count()

    if not user_proxy_count:
        return config

    proxy = choice(Proxy.objects.filter(owner=task.owner))
    if proxy.username:
        config['proxy'] = f"{proxy.username}:{proxy.password}@{proxy.host}:{proxy.port}"
    else:
        config['proxy'] = f"{proxy.host}:{proxy.port}"

    return config


def change_region(driver: Chrome, city: str) -> None:
    driver.find_element_by_class_name('geolink').click()
    sleep(1)
    city_input = driver.find_element_by_id('city__front-input')
    city_input.clear()
    city_input.send_keys(f" {city} ")
    sleep(2)

    geo_input = driver.find_element_by_class_name('input__popup_type_geo')
    localities = geo_input.find_elements_by_tag_name('li')
    for locality in localities:
        geo_data = json.loads(locality.get_attribute('data-bem'))
        item = geo_data['b-autocomplete-item']
        if item['title'] == city:
            locality.click()
            sleep(1)
            return
    sleep(1)
    city_input.send_keys(Keys.ENTER)
    sleep(1)


def trunc_url(url: str) -> str:
    url = re.sub(r'https?://', '', url)
    url = url.replace('www.', '')

    return re.sub(r'/.*', '', url)


def is_same_site(url1: str, url2: str) -> bool:
    url1 = trunc_url(url1)
    url2 = trunc_url(url2)

    return url1 == url2


def is_competitor_site(url, competitor_sites):
    competitor_urls = competitor_sites.split('\r\n')
    for site in competitor_urls:
        if is_same_site(url, site):
            return True

    return False


def walk_on_site(driver: Chrome):
    for i in range(randint(5, 15)):
        try:
            links = driver.find_elements_by_tag_name('a')

            action = ActionChains(driver)
            link = choice(links)
            action.move_to_element(link)
            action.perform()
            do_delay('fast')
            link.click()
            sleep(1)
            driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
            do_delay('fast')

            for i in range(randint(5, 40)):
                try:
                    random_div = choice(driver.find_elements_by_tag_name('div'))
                    action.move_to_element(random_div)
                    action.perform()
                    do_delay('fast')
                    driver.execute_script(f"window.scrollTo(0, {randint(1, 500)});")
                except:
                    pass
            sleep(1)
        except Exception as e:
            print(e)


def get_prestart_delay() -> int:
    if os.environ.get('SITE_WALKER_HOST') == 'DEV':
        return 0
    else:
        return randint(2*60, 20*60)


class TaskRunner(Thread):
    def __init__(self, task: Task):
        Thread.__init__(self)
        self.task = task
        self.uid = uuid4()

    def run(self):
        if self.task.launches_per_day <= self.task.launches_today:
            if self.task.launches_per_day != 0:  # 0 - there's no launch limits
                return

        if self.task.last_start is None:
            self.task.last_start = datetime(1970, 1, 1)
            self.task.save()
        if self.task.delay:
            # если с последнего запуска прошло меньше, чем delay минут
            if timezone.now() - timedelta(minutes=self.task.delay) < self.task.last_start:
                return

        self.task.is_running = True
        self.task.save()

        try:
            prestart_delay = get_prestart_delay()
            log(user=self.task.owner, task=self.task, action='TASK_ACTIVATED', uid=self.uid,
                extra={'message': f'Task will be launch in {prestart_delay} seconds'})
            sleep(prestart_delay)

            self.task.last_start = timezone.now()
            self.task.save()

            log(user=self.task.owner, task=self.task, action='LAUNCH', uid=self.uid)
            browser_configuration = generate_browser_configuration(self.task)
            driver = get_driver(browser_configuration)

            self.stalk_sites_in_yandex(driver)
            log(user=self.task.owner, task=self.task, action='FINISH', uid=self.uid)
        except Exception as e:
            logging.exception('Stalking did catch exception')
            log(user=self.task.owner, task=self.task, action='CRASHED', uid=self.uid)
        finally:
            self.task.is_running = False
            self.task.save()
            driver.close()

    def stalk_sites_in_yandex(self, driver: Chrome):
        driver.get(YANDEX_URL)

        if self.task.city != '':
            change_region(driver, self.task.city)

        driver.find_element_by_id('text').send_keys(self.task.search_query, Keys.ENTER)
        sleep(2)

        for current_page in range(10):
            result_items = driver.find_elements_by_class_name('serp-item')

            for item in result_items:
                try:
                    hyperlink = item.find_element_by_tag_name('h2')
                    links = item.find_elements_by_class_name('link_theme_outer')

                    link = links[0]
                    url = link.get_attribute('href')
                except Exception as e:
                    continue

                sleep(1)

                if is_same_site(self.task.target_url, url):
                    try:
                        hyperlink.find_element_by_tag_name('a').click()
                    except Exception as e:
                        logging.exception("URL can't be visited")

                    driver.switch_to.window(driver.window_handles[-1])

                    walk_on_site(driver)

                    log(user=self.task.owner, task=self.task, action='VISIT', extra={'visit_url': url}, uid=self.uid)
                    #  заходим на целевой сайт
                    for i in range(5):
                        driver.execute_script(f"window.scrollTo(0, {randint(300, 700)});")
                        sleep(randint(12, 24))
                    sleep(randint(10, 6 * 60))

                    break
                elif is_competitor_site(url, self.task.competitor_sites):
                    log(user=self.task.owner, task=self.task, action='VISIT', extra={'visit_url': url}, uid=self.uid)

                    link.click()
                    driver.switch_to.window(driver.window_handles[-1])
                    #  заходим к конкурентам
                    for i in range(5):
                        sleep(randint(3, 5))
                        driver.execute_script(f"window.scrollTo(0, {randint(300, 800)});")

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

            pager = driver.find_element_by_class_name('pager')
            next_page = pager.find_elements_by_tag_name('a')[-1]
            next_page.click()
            sleep(1)
            current_page_number = driver.find_element_by_class_name('pager__item_current_yes').get_attribute('innerText')
            log(user=self.task.owner, task=self.task, action='NEXT_PAGE',
                extra={'current_page': current_page_number}, uid=self.uid)


def get_driver(config: Dict) -> Chrome:
    options = ChromeOptions()

    capabilities = DesiredCapabilities.CHROME
    options.add_argument(f"--window-size={config['resolution']}")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={config['user-agent']}")
    if os.environ.get('SITE_WALKER_HOST') != 'DEV':
        options.add_argument("--headless")

    if config.get('proxy'):
        options.add_argument(f'--proxy-server={config["proxy"]}')

    return Chrome("./webdriver/chromedriver", options=options,
                  desired_capabilities=capabilities)


def log(user: User, task: Task, action: str, level: str = 'info', extra: dict = None, uid: UUID = None):
    log_entry = Log(owner=user, task=task, action=action, extra=json.dumps(extra), level=level, uid=uid)
    log_entry.save()

    logger.info(action)


def run():
    threads = {}
    try:
        for task in Task.objects.filter(status=True).filter(is_running=False):
            threads[task.id] = TaskRunner(task=task)
            threads[task.id].daemon = True
            threads[task.id].start()

        for task_id, task_runner in threads.items():
            task_runner.join()

        sleep(5)
    except KeyboardInterrupt:
        for task_id, task_runner in threads.items():
            task = Task.objects.get(pk=task_id)
            task.is_running = False
            task.save()
