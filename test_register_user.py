from browser import Browser
from dotenv import load_dotenv
from login import login
from register_user import register_user

load_dotenv()

def test_register_user():
    browser = Browser()
    login(browser)
    assert register_user(browser)

