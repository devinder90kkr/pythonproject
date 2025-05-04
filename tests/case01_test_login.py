import pytest
import json
import os
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.case01_login_page import LoginPage
from configparser import ConfigParser
from utils.extent_report_manager import ExtentReportManager
import time
import logging

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory().get_driver()
    logger = Logger()
    login_page = LoginPage(driver)
    extent_report = ExtentReportManager.get_instance()
    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.login_page = login_page
    request.cls.extent_report = extent_report
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
@pytest.mark.smoke
class TestLogin:
    def test_valid_login(self):
        """Test login with valid credentials"""
        self.extent_report.start_test("Valid Login Test", "Testing login with valid credentials")
        self.logger.info("Starting valid login test")
        try:
            # Navigate to login page
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.extent_report.log_info("Navigated to login page")
            self.logger.info("Navigated to login page")
            
            # Use LoginPage methods for login
            self.extent_report.log_info("Attempting to login with valid credentials")
            self.logger.info("Attempting to login with valid credentials")
            self.login_page.login(
                self.test_data['login']['valid_username'],
                self.test_data['login']['valid_password']
            )

            # Take screenshot of successful login
            self.login_page.take_screenshot("valid_login_success")
            self.extent_report.add_screenshot("reports/screenshots/valid_login_success.png", "Login Success")
            self.extent_report.log_pass("Login successful with valid credentials")
            self.logger.info("Valid login test completed successfully")
            
        except Exception as e:
            self.extent_report.log_fail(f"Test failed: {str(e)}")
            self.logger.error(f"Test failed: {str(e)}")
            self.login_page.take_screenshot("valid_login_failure")
            self.extent_report.add_screenshot("reports/screenshots/valid_login_failure.png", "Login Failure")
            raise
        finally:
            self.extent_report.end_test() 