import pytest
import json
import os
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from pages.case01_login_page import LoginPage
from configparser import ConfigParser
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = DriverFactory().get_driver()
    login_page = LoginPage(driver)
    request.cls.driver = driver
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
        try:
            # Navigate to login page
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            # Use LoginPage methods for login
            self.login_page.login(
                self.test_data['login']['valid_username'],
                self.test_data['login']['valid_password']
            )
        except Exception as e:
            raise

    def test_invalid_username(self):
        """Test login with invalid username"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['invalid_username'],
                self.test_data['login']['valid_password']
            )
        except Exception as e:
            raise

    def test_invalid_password(self):
        """Test login with invalid password"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['valid_username'],
                self.test_data['login']['invalid_password']
            )
        except Exception as e:
            raise

    def test_empty_username(self):
        """Test login with empty username"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                "",
                self.test_data['login']['valid_password']
            )
        except Exception as e:
            raise

    def test_empty_password(self):
        """Test login with empty password"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['valid_username'],
                ""
            )
        except Exception as e:
            raise

    def test_special_characters(self):
        """Test login with special characters"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['special_chars_username'],
                self.test_data['login']['special_chars_password']
            )
        except Exception as e:
            raise

    def test_sql_injection(self):
        """Test login with SQL injection attempt"""
        try:
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.login_page.login(
                self.test_data['login']['sql_injection_username'],
                self.test_data['login']['sql_injection_password']
            )
        except Exception as e:
            raise