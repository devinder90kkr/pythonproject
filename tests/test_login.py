import pytest
import json
import os
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.login_page import LoginPage
from configparser import ConfigParser
import time
import logging

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory().get_driver()
    logger = Logger()
    login_page = LoginPage(driver)
    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.login_page = login_page
    request.cls.config = load_config()
    request.cls.test_data = load_test_data()
    yield
    driver.quit()

def load_config():
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
    config.read(config_path)
    return config

def load_test_data():
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'test_data.json'), 'r') as f:
        return json.load(f)

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login(self):
        self.logger.info("Starting valid login test")
        try:
            # Navigate to login page
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.logger.info("Navigated to login page")
            # Use LoginPage methods for login
            self.logger.info("Attempting to login with valid credentials")
            self.login_page.login(
                self.test_data['login']['valid_username'],
                self.test_data['login']['valid_password']
            )
            # Explicitly check for staff details
            self.logger.info("Checking for staff details after login")
            staff_details_present = self.login_page.is_staff_details_present()
            self.logger.info(f"Staff details check result: {staff_details_present}")
            
            # Assert staff details are present
            assert staff_details_present, "Staff details not found after login"
            self.logger.info("Staff details found successfully")
            
            # Take screenshot of successful login
            self.login_page.take_screenshot("valid_login_success")
            self.logger.info("Screenshot captured for successful login")
            self.logger.info("Valid login test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.login_page.take_screenshot("valid_login_failure")
            self.logger.error("Screenshot captured for failed login")
            raise 