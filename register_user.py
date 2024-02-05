from os import getenv
from selenium.webdriver.common.by import By
from browser import Browser
from faker import Faker
import random
import string
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.request import Request
from time import sleep


def gen_fake_user() -> dict:
    faker = Faker()
    user = {
        "name": faker.name(),
        "email": faker.email(),
        "phone": '(12) 3 2313-1231',
        "password": ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    }
    return user


def select_type_user(browser: Browser, type: str):
    select = browser.driver.find_element(By.ID, 'type_user')
    browser.actions.move_to_element(select).click().perform()
    
    if type.lower() == "controlador":
        browser.actions.send_keys(Keys.DOWN).perform()
    elif type.lower() == "administrador":
        browser.actions.send_keys(Keys.DOWN).send_keys(Keys.DOWN).perform()    
    
    browser.actions.send_keys(Keys.ENTER).perform()

    
def get_request_register_user(browser: Browser) -> Request:
    for request in browser.driver.requests:
        if request.method == "POST" and request.url.endswith('/users'):
            return request
    return None
    

def register_user(browser: Browser) -> bool:
    browser.driver.get(f"{getenv('HOME_PAGE')}/userregister")
    user = gen_fake_user()
    browser.driver.find_element(By.ID, 'username').send_keys(user["name"])
    browser.driver.find_element(By.ID, 'email').send_keys(user["email"])
    
    phone = browser.driver.find_element(By.ID, 'phone')
    browser.actions.move_to_element(phone).click().send_keys("9", "9", "9", "9", "9", "9", "9", "9", "9", "9", "9").perform()
    
    browser.driver.find_element(By.ID, 'password').send_keys(user["password"])
    browser.driver.find_element(By.ID, 'confirm_password').send_keys(user["password"])
    select_type_user(browser, "administrador")
    browser.driver.find_element(By.ID, 'confirm').click()
    browser.wait.until(EC.presence_of_element_located((By.ID, "btn_confirm_dialog")))
    browser.driver.find_element(By.ID, 'btn_confirm_dialog').click()
    
    # Espera fazer a requisição
    sleep(1)
    
    request = get_request_register_user(browser)
    if request == None:
        return False
    return request.response.status_code == 200
    
