from browser import Browser
from dotenv import load_dotenv
from login import login
import complaint

load_dotenv()


def test_occurrence_no_location():
    browser = Browser()
    login(browser)
    assert complaint.no_location(browser) == 29
