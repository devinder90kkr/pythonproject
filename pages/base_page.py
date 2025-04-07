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
        self.logger = None  # Will be set by the test class

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
        """
        Click on an element
        """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        Send keys to an element
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        """
        Check if element is present
        """
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def clear_field(self, locator):
        """
        Clear input field
        """
        element = self.find_element(locator)
        element.clear()

    def get_element_text(self, locator):
        """
        Get text from an element
        """
        try:
            element = self.find_element(locator)
            return element.text
        except TimeoutException:
            self.logger.error(f"Element not found: {locator}")
            return ""

    def take_screenshot(self, name):
        """
        Take screenshot and save it
        """
        try:
            # Create screenshots directory if it doesn't exist
            screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'screenshots')
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            
            # Generate filename with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            
            # Take screenshot
            self.driver.save_screenshot(filepath)
            self.logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            self.logger.error(f"Failed to take screenshot: {str(e)}")
            raise 