import logging
import random
import re
from random import randint, choice
from time import sleep
from threading import Thread
from typing import Dict
from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions, DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType, Proxy as WebDriverProxy
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
YANDEX_URL = 'https://yandex.ru'


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


def generate_browser_configuration(task: Task) -> Dict[str, str]:
    config = {'user-agent': generate_user_agent(),
              'resolution': get_random_screen_resolution()}

    user_proxy_count = Proxy.objects.filter(owner=task.owner).count()

    if not user_proxy_count:
        return config

    proxy = choice(Proxy.objects.filter(owner=task.owner))
    config['proxy'] = f"http://{proxy.username}:{proxy.password}@{proxy.host}:{proxy.port}"

    return config


def change_region(driver: Chrome, region: str):
    driver.find_element_by_class_name('geolink').click()
    sleep(1)
    city_input = driver.find_element_by_id('city__front-input')
    city_input.clear()
    city_input.send_keys(region)
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
        links = driver.find_elements_by_tag_name('a')

        action = ActionChains(driver)
        link = choice(links)
        action.move_to_element(link)
        action.perform()
        sleep(randint(5, 10))
        link.click()
        sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        sleep(randint(3, 7))


class TaskRunner(Thread):
    def __init__(self, task: Task):
        Thread.__init__(self)
        self.task = task

    def run(self):
        sleep(randint(2*60, 20*60))
        if self.task.last_start is None:
            self.task.last_start = datetime(1970, 1, 1)
            self.task.save()
        if self.task.delay:
            # если с последнего запуска прошло меньше, чем delay минут
            if timezone.now() - timedelta(minutes=self.task.delay) < self.task.last_start:
                return
        self.task.last_start = timezone.now()
        self.task.save()

        user = self.task.owner
        log(user, f'Task {self.task.id} started. Target site: {self.task.target_url}')
        browser_configuration = generate_browser_configuration(self.task)
        driver = get_driver(browser_configuration)
        driver.get(YANDEX_URL)

        if self.task.region.name != '':
            change_region(driver, self.task.region.name)

        driver.find_element_by_id('text').send_keys(self.task.search_query, Keys.ENTER)
        # driver.save_screenshot(SCREENSHOTS_DIR + f'screenshot_{datetime.now()}.png')
        sleep(2)

        result_items = driver.find_elements_by_class_name('serp-item')

        for item in result_items:
            hyperlink = item.find_element_by_tag_name('h2')
            links = item.find_elements_by_class_name('link_theme_outer')

            try:
                link = links[0]
                url = link.get_attribute('href')
            except:
                continue

            sleep(1)

            if is_same_site(self.task.target_url, url):
                hyperlink.find_element_by_tag_name('a').click()

                driver.switch_to.window(driver.window_handles[-1])

                walk_on_site(driver)

                log(user,
                    f"Task {self.task.id}, visit url: {url}, target site: {self.task.target_url}, task {self.task.id}")
                #  заходим на целевой сайт
                for i in range(5):
                    driver.execute_script(f"window.scrollTo(0, {randint(300, 700)});")
                    # driver.save_screenshot(SCREENSHOTS_DIR + f'screenshot_{datetime.now()}.png')
                    sleep(randint(12, 24))

                sleep(randint(3*60, 6*60))

                break
            elif is_competitor_site(url, self.task.competitor_sites):
                log(user,
                    f"Task {self.task.id}, visit url: {url}, target site: {self.task.target_url}, task {self.task.id}")

                link.click()
                driver.switch_to.window(driver.window_handles[-1])
                #  заходим к конкурентам
                for i in range(5):
                    sleep(randint(3, 5))
                    driver.execute_script(f"window.scrollTo(0, {randint(300, 800)});")

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        driver.close()


def get_driver(config: Dict) -> Chrome:
    options = ChromeOptions()
    capabilities = DesiredCapabilities.CHROME
    options.add_argument(f"--window-size={config['resolution']}")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={config['user-agent']}")
    options.add_argument("--headless")

    if config.get('proxy'):
        proxy = WebDriverProxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': config['proxy']
        })
        proxy.add_to_capabilities(capabilities)

    return Chrome("./webdriver/chromedriver", options=options,
                  desired_capabilities=capabilities)


def log(user: User, action: str, level='info'):
    log_entry = Log(owner=user, action=action)
    log_entry.save()

    logger.info(action)


def run():
    threads = {}
    for task in Task.objects.filter(status=True):
        threads[task.id] = TaskRunner(task=task)
        threads[task.id].daemon = True
        threads[task.id].start()

    for task_id, task_runner in threads.items():
        task_runner.join()

    sleep(5)
