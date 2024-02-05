from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from browser import Browser
import os

def login(browser: Browser):

    # Abre a página desejada
    browser.driver.get(f"{os.getenv('HOME_PAGE')}")

    # Encontra o campo de e-mail e preenche com o e-mail fornecido
    email_field = browser.driver.find_element(By.XPATH, "//div[contains(@class, 'MuiFormControl-root')][1]//input")
    email_field.clear()
    email_field.send_keys(f"{os.getenv('ADMIN_EMAIL')}")

    # Encontra o campo de senha e preenche com a senha fornecida
    password_field = browser.driver.find_element(By.XPATH, "//div[contains(@class, 'MuiFormControl-root')][2]//input")
    password_field.clear()
    password_field.send_keys(f"{os.getenv('ADMIN_PASSWORD')}")

    # Encontra o botão de login e clica nele
    login_button = browser.driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    try:
        browser.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Ocorrências Comuns')]")))
        return True
    except:
        return False