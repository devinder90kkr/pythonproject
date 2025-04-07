import pytest
import json
import os
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.login_page import LoginPage
from configparser import ConfigParser

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
class TestInvalidLogin:
    def test_invalid_credentials(self):
        self.logger.info("Starting invalid login test")
        try:
            # Navigate to login page
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            
            # Perform login with invalid credentials
            self.login_page.login(
                self.test_data['login']['invalid_username'],
                self.test_data['login']['invalid_password']
            )
            
            # Verify error message
            assert self.login_page.is_error_message_present(), "Error message not displayed"
            self.logger.info("Invalid login test passed")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.login_page.take_screenshot("invalid_login_failure")
            raise 