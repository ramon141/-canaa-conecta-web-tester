import time
from os import getenv
from selenium.webdriver.common.by import By
from browser import Browser


def set_report_message(browser: Browser) -> str:
    browser.driver.get(f"{getenv('HOME_PAGE')}/details/{getenv('OCCURRENCE_REPORT')}")
    browser.driver.find_element(By.ID, 'report_area').send_keys(getenv('MESSAGE_OCCURRENCE_REPORT'))
    browser.driver.find_element(By.ID, 'report_button').click()
    time.sleep(0.5)
    browser.driver.find_element(By.ID, 'btn_confirm_dialog').click()

def get_last_report_message(browser: Browser) -> str:
    browser.driver.get(f"{getenv('HOME_PAGE')}/details/{getenv('OCCURRENCE_REPORT')}")
    time.sleep(1)
    messages = browser.driver.find_elements(By.CSS_SELECTOR, 'div#list_report_messages > div > div > div > div > div > div > p > span')
    
    last_message = messages[-1].text
    
    return last_message