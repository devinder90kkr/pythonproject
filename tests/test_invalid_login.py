import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.base_page import BasePage
from configparser import ConfigParser
import json
import os
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def setup(request):
    """
    Setup fixture for invalid login tests
    """
    driver = DriverFactory().get_driver()
    logger = Logger()
    base_page = BasePage(driver)
    
    # Store in request context
    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.base_page = base_page
    request.cls.config = load_config()
    request.cls.test_data = load_test_data()
    
    yield
    
    # Teardown
    driver.quit()

def load_config():
    """
    Load configuration from config.ini
    """
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
    config.read(config_path)
    return config

def load_test_data():
    """
    Load test data from test_data.json
    """
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'test_data.json'), 'r') as f:
        return json.load(f)

@pytest.mark.usefixtures("setup")
class TestInvalidLogin:
    """
    Test class for invalid login scenarios
    """
    def test_invalid_credentials(self):
        """
        Test login with invalid credentials
        """
        login_page = LoginPage(self.driver)
        login_page.logger = self.logger
        login_page.base_page = self.base_page
        
        # Test invalid username
        login_page.enter_username(self.test_data['invalid_username'])
        login_page.enter_password(self.test_data['valid_password'])
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_error_message_visible(), "Error message not visible for invalid username"
        error_text = login_page.get_error_message_text()
        assert "Given email or password does not match" in error_text, "Incorrect error message for invalid username"
        
        # Clear fields
        login_page.clear_username()
        login_page.clear_password()
        
        # Test invalid password
        login_page.enter_username(self.test_data['valid_username'])
        login_page.enter_password(self.test_data['invalid_password'])
        login_page.click_login_button()
        
        # Verify error message
        assert login_page.is_error_message_visible(), "Error message not visible for invalid password"
        error_text = login_page.get_error_message_text()
        assert "Given email or password does not match" in error_text, "Incorrect error message for invalid password"
        
        self.logger.info("Invalid credentials test completed successfully")

    def test_empty_credentials(self):
        """
        Test login with empty credentials
        """
        self.logger.info("Starting empty credentials test")
        try:
            # Navigate to login page
            self.driver.get(self.config.get('ENVIRONMENT', 'base_url') + '/login')
            self.logger.info("Navigated to login page")
            
            # Click login without entering credentials
            login_button = (By.XPATH, "//button[normalize-space()='Login']")
            self.base_page.click(login_button)
            self.logger.info("Clicked login button without credentials")
            
            # Verify error messages for empty fields
            username_error = (By.XPATH, "//span[@class='error d-block' and contains(text(), 'Email is required')]")
            password_error = (By.XPATH, "//span[@class='error d-block' and contains(text(), 'Password is required')]")
            
            assert self.base_page.is_element_present(username_error), "Email required error not displayed"
            assert self.base_page.is_element_present(password_error), "Password required error not displayed"
            
            self.logger.info("Error messages displayed for empty credentials")
            self.base_page.take_screenshot("empty_credentials_error")
            
            self.logger.info("Empty credentials test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.base_page.take_screenshot("empty_credentials_failure")
            raise 