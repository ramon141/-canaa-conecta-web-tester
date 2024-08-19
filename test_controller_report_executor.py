from browser import Browser
from dotenv import load_dotenv
from login import login
from register_report import set_report_message, get_last_report_message
import os

load_dotenv()

def test_controller_report_executor():
    browser = Browser()
    login(browser, os.getenv('CONTROLLER_EMAIL'), os.getenv('CONTROLLER_PASSWORD'))
    set_report_message(browser)
    login(browser, os.getenv('EXECUTOR_EMAIL'), os.getenv('EXECUTOR_PASSWORD'))
    assert get_last_report_message(browser) == os.getenv('MESSAGE_OCCURRENCE_REPORT')

