import time
from os import getenv
from seleniumwire.request import Request
from browser import Browser
import json


def get_request_complaints(browser: Browser) -> Request | None:
    for request in browser.driver.requests:
        if request.method == "GET" and "/admin/complaints" in request.url:
            return request
    return None


def no_location(browser: Browser):
    browser.driver.get(f"{getenv('HOME_PAGE')}/no-location-complaints")
    request = None
    while request is None:
        print("Testing occurrence")
        request = get_request_complaints(browser)
        time.sleep(0.5)
    body = request.response.body.decode('utf-8')
    data = json.loads(body)

    return len(data)
