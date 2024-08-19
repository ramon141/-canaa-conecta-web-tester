from browser import Browser
from dotenv import load_dotenv
from login import login
from register_user import register_user
import os

load_dotenv()

def test_login():
    browser = Browser()
    assert login(browser, os.getenv('ADMIN_EMAIL'), os.getenv('ADMIN_PASSWORD'))