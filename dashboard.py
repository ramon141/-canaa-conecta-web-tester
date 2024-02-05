import time
from os import getenv
from selenium.webdriver.common.by import By
from browser import Browser


def get_box_info(browser: Browser, path: str) -> str:
    browser.driver.get(f"{getenv('HOME_PAGE')}/dashboard")

    result = '0'
    max_iterations = 30
    while result == '0' and max_iterations > 0:
        result = browser.driver.find_element(By.XPATH, path).text
        max_iterations -= 1
        time.sleep(0.5)

    return result


def get_quant_occurrences_attendance(browser: Browser) -> str:
    return get_box_info(browser, '//*[@id="occurrences-solved-dashboard"]/div/div/div/div/h3')


def get_quant_occurrences_open(browser: Browser) -> str:
    return get_box_info(browser, '//*[@id="occurrences-open-dashboard"]/div/div/div/div/h3')
