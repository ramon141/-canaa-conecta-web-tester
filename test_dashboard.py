from browser import Browser
from dotenv import load_dotenv
from login import login
from dashboard import get_quant_occurrences_attendance, get_quant_occurrences_open

load_dotenv()


def test_occurrence_attendance():
    browser = Browser()
    login(browser)
    assert get_quant_occurrences_attendance(browser) == '1416'


def test_occurrences_open():
    browser = Browser()
    login(browser)
    assert get_quant_occurrences_open(browser) == '1204'
