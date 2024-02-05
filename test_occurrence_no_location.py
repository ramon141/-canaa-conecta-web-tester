from browser import Browser
from dotenv import load_dotenv
from login import login
import complaint

load_dotenv()


def test_occurrence_no_location():
    browser = Browser()
    login(browser)
    assert complaint.no_location(browser) == 29


def test_occurrence_no_location_with_filter():
    browser = Browser()
    login(browser)
    assert complaint.no_location_with_filter(browser, 'M1502152-20240131-690882') == 1
