from browser import Browser
import os
from dotenv import load_dotenv
from login import login
from register_user import register_user
from time import sleep

load_dotenv()


browser = Browser()
login(browser)
print(register_user(browser))
# sleep(10)
