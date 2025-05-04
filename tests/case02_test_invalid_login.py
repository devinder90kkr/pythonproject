import pytest
import json
import os
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.case01_login_page import LoginPage
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
@pytest.mark.smoke
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

            # Take screenshot of successful login
            self.login_page.take_screenshot("valid_login_success")
            self.logger.info("Screenshot captured for successful login")
            self.logger.info("Valid login test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.login_page.take_screenshot("valid_login_failure")
            self.logger.error("Screenshot captured for failed login")
            raise

    def test_invalid_username(self):
        """Test login with invalid username"""
        self.logger.info("Starting invalid username test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['invalid_username'],
                self.test_data['login']['valid_password']
            )
            self.login_page.take_screenshot("invalid_username")
            self.logger.info("Invalid username test completed")
        except Exception as e:
            self.logger.error(f"Invalid username test failed: {str(e)}")
            self.login_page.take_screenshot("invalid_username_failure")
            raise

    def test_invalid_password(self):
        """Test login with invalid password"""
        self.logger.info("Starting invalid password test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['valid_username'],
                self.test_data['login']['invalid_password']
            )
            self.login_page.take_screenshot("invalid_password")
            self.logger.info("Invalid password test completed")
        except Exception as e:
            self.logger.error(f"Invalid password test failed: {str(e)}")
            self.login_page.take_screenshot("invalid_password_failure")
            raise

    def test_empty_username(self):
        """Test login with empty username"""
        self.logger.info("Starting empty username test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                "",
                self.test_data['login']['valid_password']
            )
            self.login_page.take_screenshot("empty_username")
            self.logger.info("Empty username test completed")
        except Exception as e:
            self.logger.error(f"Empty username test failed: {str(e)}")
            self.login_page.take_screenshot("empty_username_failure")
            raise

    def test_empty_password(self):
        """Test login with empty password"""
        self.logger.info("Starting empty password test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['valid_username'],
                ""
            )
            self.login_page.take_screenshot("empty_password")
            self.logger.info("Empty password test completed")
        except Exception as e:
            self.logger.error(f"Empty password test failed: {str(e)}")
            self.login_page.take_screenshot("empty_password_failure")
            raise

    def test_special_characters(self):
        """Test login with special characters"""
        self.logger.info("Starting special characters test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['special_chars_username'],
                self.test_data['login']['special_chars_password']
            )
            self.login_page.take_screenshot("special_chars")
            self.logger.info("Special characters test completed")
        except Exception as e:
            self.logger.error(f"Special characters test failed: {str(e)}")
            self.login_page.take_screenshot("special_chars_failure")
            raise

    def test_sql_injection(self):
        """Test login with SQL injection attempt"""
        self.logger.info("Starting SQL injection test")
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['sql_injection_username'],
                self.test_data['login']['sql_injection_password']
            )
            self.login_page.take_screenshot("sql_injection")
            self.logger.info("SQL injection test completed")
        except Exception as e:
            self.logger.error(f"SQL injection test failed: {str(e)}")
            self.login_page.take_screenshot("sql_injection_failure")
            raise