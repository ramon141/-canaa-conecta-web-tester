# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import os
from selenium.webdriver import ActionChains


class Browser:
    def __init__(self) -> None:
        # Instala automaticamente o chromedriver
        chromedriver_autoinstaller.install()
        
        options = webdriver.ChromeOptions()
        
        if os.getenv("ENV").lower() == "prod":
            options.add_argument( '--headless')

        # Define o navegador (neste caso, o Chrome)
        self.driver = webdriver.Chrome(options=options)
        
        self.wait = WebDriverWait(self.driver, 10)
        
        self.actions = ActionChains(self.driver)

    
    def get_driver(self) -> webdriver.Chrome:
        return self.driver
    
    def get_wait(self) -> WebDriverWait:
        return self.wait
    
    def get_actions(self) -> ActionChains:
        return self.actions