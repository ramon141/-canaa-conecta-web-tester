from browser import Browser
from dotenv import load_dotenv
from login import login
import complaint
from os import getenv

load_dotenv()


def test_occurrence_no_location():
    browser = Browser()
    login(browser)
    assert str(complaint.no_location(browser)) == getenv('TABLE_NO_LOCATION')


def test_occurrence_no_location_with_filter():
    browser = Browser()
    login(browser)
    assert complaint.no_location_with_filter(browser, getenv('TABLE_NO_LOCATION_FILTER')) == 1
