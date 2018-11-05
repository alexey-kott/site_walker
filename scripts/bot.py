import os
import logging
from pathlib import Path
import random
from time import sleep
from threading import Thread
from datetime import datetime
from typing import List, Dict


from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from user_agent import generate_user_agent

from walker_panel.models import Task

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./logs/err.log')

SCREENSHOTS_DIR = './screenshots/'


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


def generate_browser_configuration() -> Dict[str, str]:
    config = {'user-agent': generate_user_agent(),
              'resolution': get_random_screen_resolution()}

    return config


class TaskRunner(Thread):
    def __init__(self, search_query: str, target_url: str, competitor_sites: List[str]):
        Thread.__init__(self)
        self.search_query = search_query
        self.target_url = target_url
        self.competitor_sites = competitor_sites

    def run(self):
        browser_configuration = generate_browser_configuration()
        print(browser_configuration)
        driver = get_driver(browser_configuration)
        driver.get('https://yandex.ru')
        sleep(2)

        driver.find_element_by_id('text').send_keys(self.search_query, Keys.ENTER)
        driver.save_screenshot(SCREENSHOTS_DIR + f'screenshot_{datetime.now()}.png')
        sleep(3)

        result_items = driver.find_elements_by_class_name('serp-item')

        for item in result_items:
            links = item.find_elements_by_class_name('link_theme_outer')
            try:
                link = links[0]
            except:
                continue

            url = link.find_element_by_tag_name('b').get_attribute('innerText')
            print(url)
            # print(link.get_property('outerHTML'))




        driver.close()


def get_driver(config: Dict) -> Chrome:
    options = ChromeOptions()
    options.add_argument(f"--window-size={config['resolution']}")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={config['user-agent']}")
    options.add_argument("--headless")

    return Chrome("./webdriver/chromedriver", options=options)


def run():
    threads = {}
    for task in Task.objects.all():
        competitor_sites = task.competitor_sites.split('\r\n')

        threads[task.id] = TaskRunner(search_query=task.search_query,
                                      target_url=task.target_url,
                                      competitor_sites=competitor_sites)

        threads[task.id].start()

        sleep(3)
