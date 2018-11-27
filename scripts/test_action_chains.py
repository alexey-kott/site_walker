from time import sleep

import numpy as np
import scipy.interpolate as si
from selenium.webdriver import Chrome, ChromeOptions, ActionChains


def get_driver() -> Chrome:
    options = ChromeOptions()
    options.add_argument(f"--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-position=1920,0")

    return Chrome("./webdriver/chromedriver", options=options)


from random import randint

def get_curves():
    # curve base
    # points = [[0, 0], [24, 12], [14, 13], [11, 1], ]  # curve base
    points = [[randint(0, 100), randint(0, 100)] for i in range(20)]
    points = np.array(points)

    x = points[:, 0]
    y = points[:, 1]

    t = range(len(points))
    ipl_t = np.linspace(0.0, len(points) - 1, 100)

    x_tup = si.splrep(t, x, k=3)
    y_tup = si.splrep(t, y, k=3)

    x_list = list(x_tup)
    xl = x.tolist()
    x_list[1] = xl + [0.0, 0.0, 0.0, 0.0]

    y_list = list(y_tup)
    yl = y.tolist()
    y_list[1] = yl + [0.0, 0.0, 0.0, 0.0]

    x_i = si.splev(ipl_t, x_list)  # x interolate values
    y_i = si.splev(ipl_t, y_list)  # y_interpolate values

    return x_i, y_i


def run():

    driver = get_driver()
    url = "https://codepen.io/falldowngoboone/pen/PwzPYv"
    url = "https://codepen.io/falldowngoboone/full/PwzPYv/"
    driver.get(url)

    x_i, y_i = get_curves()

    action = ActionChains(driver)
    startElement = driver.find_element_by_id('result-iframe-wrap')
    # First, go to your start point or Element
    action.move_to_element(startElement)
    action.perform()

    for mouse_x, mouse_y in sorted(zip(x_i, y_i), reverse=True):
        action.move_by_offset(mouse_x, mouse_y)
        action.perform()
        sleep(0.1)
        print(mouse_x, mouse_y)
        # sleep(1)


