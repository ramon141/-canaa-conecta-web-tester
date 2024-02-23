import time
from os import getenv

from selenium.webdriver.common.by import By
from seleniumwire.request import Request
from browser import Browser
import json


def get_request_complaints(browser: Browser) -> Request | None:
    for request in browser.driver.requests:
        if request.method == "GET" and "/admin/complaints" in request.url:
            return request
    return None


def no_location(browser: Browser) -> int:
    browser.driver.get(f"{getenv('HOME_PAGE')}/no-location-complaints")
    request = None
    while request is None or request.response is None:
        print("Testing occurrence")
        request = get_request_complaints(browser)
        time.sleep(0.5)

    body = request.response.body.decode('utf-8')
    data = json.loads(body)

    return len(data)


def no_location_with_filter(browser: Browser, filter: str) -> int:
    browser.driver.get(f"{getenv('HOME_PAGE')}/no-location-complaints")

    # Espera carregar as ocorrências
    request = None
    while request is None or request.response is None:
        request = get_request_complaints(browser)
        time.sleep(0.5)

    time.sleep(1)
    browser.driver.find_element(By.ID, 'search_table').send_keys(filter)
    browser.driver.find_element(By.XPATH, '//*[@id="table-occurrences-input"]/div[2]/button').click()

    time.sleep(0.5)

    quant_rows = browser.driver.execute_script('''
            const table = document.getElementsByTagName("table")[0];
            return table.children[1].childElementCount;
    ''')

    return quant_rows
