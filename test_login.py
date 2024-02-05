from browser import Browser
from dotenv import load_dotenv
from login import login
from register_user import register_user

load_dotenv()

def test_login():
    browser = Browser()
    assert login(browser)