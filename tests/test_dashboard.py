import pytest
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from configparser import ConfigParser
import json
import os
import time

@pytest.fixture(scope="class")
def setup(request):
    """
    Setup fixture for dashboard tests
    """
    driver = DriverFactory().get_driver()
    logger = Logger()
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    
    # Store in request context
    request.cls.driver = driver
    request.cls.logger = logger
    request.cls.login_page = login_page
    request.cls.dashboard_page = dashboard_page
    request.cls.config = load_config()
    request.cls.test_data = load_test_data()
    
    # Perform login first
    try:
        request.cls.logger.info("Starting dashboard test setup")
        # Navigate to login page
        driver.get(request.cls.config.get('ENVIRONMENT', 'base_url') + '/login')
        request.cls.logger.info("Navigated to login page")
        
        # Perform login
        request.cls.logger.info("Attempting to login with valid credentials")
        login_page.login(
            request.cls.test_data['login']['valid_username'],
            request.cls.test_data['login']['valid_password']
        )
        
        # Verify login was successful by checking for staff details
        request.cls.logger.info("Checking for staff details after login")
        staff_details_present = login_page.is_staff_details_present()
        request.cls.logger.info(f"Staff details check result: {staff_details_present}")
        
        if not staff_details_present:
            raise Exception("Login failed - staff details not found")
            
        request.cls.logger.info("Login successful, proceeding with dashboard tests")
        
    except Exception as e:
        request.cls.logger.error(f"Setup failed: {str(e)}")
        login_page.take_screenshot("dashboard_setup_failure")
        raise
    
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
@pytest.mark.smoke
class TestDashboard:
    """
    Test class for dashboard functionality
    """
    def test_check_and_click_schedule_master(self):
        """
        Test checking and clicking Schedule Master menu
        """
        self.logger.info("Starting Schedule Master menu check and click test")
        try:
            # Check and click the menu
            result = self.dashboard_page.check_and_click_menu(
                self.dashboard_page.locators.SCHEDULE_MASTER,
                "Schedule Master"
            )
            assert result, "Failed to check and click Schedule Master menu"
            
            # Add a small delay to see the result
            time.sleep(2)
            
            self.logger.info("Schedule Master menu check and click test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.dashboard_page.take_screenshot("schedule_master_check_click_failure")
            raise

    def test_check_and_click_member_communication(self):
        """
        Test checking and clicking Member Communication menu
        """
        self.logger.info("Starting Member Communication menu check and click test")
        try:
            # Check and click the menu
            result = self.dashboard_page.check_and_click_menu(
                self.dashboard_page.locators.MEMBER_COMMUNICATION,
                "Member Communication"
            )
            assert result, "Failed to check and click Member Communication menu"
            
            # Add a small delay to see the result
            time.sleep(2)
            
            self.logger.info("Member Communication menu check and click test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.dashboard_page.take_screenshot("member_communication_check_click_failure")
            raise

    def test_check_and_click_member_summary(self):
        """
        Test checking and clicking Member Summary menu
        """
        self.logger.info("Starting Member Summary menu check and click test")
        try:
            # Check and click the menu
            result = self.dashboard_page.check_and_click_menu(
                self.dashboard_page.locators.MEMBER_SUMMARY,
                "Member Summary"
            )
            assert result, "Failed to check and click Member Summary menu"
            
            # Add a small delay to see the result
            time.sleep(2)
            
            self.logger.info("Member Summary menu check and click test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.dashboard_page.take_screenshot("member_summary_check_click_failure")
            raise

    def test_check_and_click_member_call(self):
        """
        Test checking and clicking Member Call menu
        """
        self.logger.info("Starting Member Call menu check and click test")
        try:
            # Check and click the menu
            result = self.dashboard_page.check_and_click_menu(
                self.dashboard_page.locators.MEMBER_CALL,
                "Member Call"
            )
            assert result, "Failed to check and click Member Call menu"
            
            # Add a small delay to see the result
            time.sleep(2)
            
            self.logger.info("Member Call menu check and click test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.dashboard_page.take_screenshot("member_call_check_click_failure")
            raise

    def test_check_and_click_guide_sound(self):
        """
        Test checking and clicking Guide Sound menu
        """
        self.logger.info("Starting Guide Sound menu check and click test")
        try:
            # Check and click the menu
            result = self.dashboard_page.check_and_click_menu(
                self.dashboard_page.locators.GUIDE_SOUND,
                "Guide Sound"
            )
            assert result, "Failed to check and click Guide Sound menu"
            
            # Add a small delay to see the result
            time.sleep(2)
            
            self.logger.info("Guide Sound menu check and click test completed successfully")
            
        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            self.dashboard_page.take_screenshot("guide_sound_check_click_failure")
            raise