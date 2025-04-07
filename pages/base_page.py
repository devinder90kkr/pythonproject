from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
from configparser import ConfigParser
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.config = ConfigParser()
        self.config.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini'))
        self.wait = WebDriverWait(self.driver, int(self.config.get('TIMEOUTS', 'explicit_wait')))

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element not found: {locator}")

    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Elements not found: {locator}")

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, name):
        screenshot_dir = self.config.get('REPORTS', 'screenshot_path')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        self.driver.save_screenshot(screenshot_path)
        return screenshot_path 