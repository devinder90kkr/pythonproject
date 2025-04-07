from pages.base_page import BasePage
from pages.locators.login_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger
import time

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
        self.logger = Logger()
        
    def check_and_click_menu(self, locator, menu_name):
        """
        Check if menu is available and click it
        """
        try:
            self.logger.info(f"Checking and clicking {menu_name} menu")
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            self.logger.info(f"{menu_name} menu is available")
            element.click()
            self.logger.info(f"Successfully clicked {menu_name} menu")
            # Take screenshot after click
            self.take_screenshot(f"{menu_name.lower().replace(' ', '_')}_clicked")
            return True
        except Exception as e:
            self.logger.error(f"Failed to check/click {menu_name} menu: {str(e)}")
            self.take_screenshot(f"{menu_name.lower().replace(' ', '_')}_click_failed")
            return False
            
    def is_schdule_master_menu_present(self):
        """
        Check if Schedule master menu is present
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.SCHEDULE_MASTER)
            )
            self.logger.info("Schedule master menu is present")
            return True
        except Exception as e:
            self.logger.error(f"Schedule master menu not found: {str(e)}")
            return False
            
    def is_member_communication_menu_present(self):
        """
        Check if Member Communication menu is present
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.MEMBER_COMMUNICATION)
            )
            self.logger.info("Member Communication menu is present")
            return True
        except Exception as e:
            self.logger.error(f"Member Communication menu not found: {str(e)}")
            return False
            
    def is_member_summary_menu_present(self):
        """
        Check if Member Summary menu is present
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.MEMBER_SUMMARY)
            )
            self.logger.info("Member Summary menu is present")
            return True
        except Exception as e:
            self.logger.error(f"Member Summary menu not found: {str(e)}")
            return False
            
    def is_member_call_menu_present(self):
        """
        Check if Member Call menu is present
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.MEMBER_CALL)
            )
            self.logger.info("Member Call menu is present")
            return True
        except Exception as e:
            self.logger.error(f"Member Call menu not found: {str(e)}")
            return False
            
    def is_guide_sound_menu_present(self):
        """
        Check if Guide Sound menu is present
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.locators.GUIDE_SOUND)
            )
            self.logger.info("Guide Sound menu is present")
            return True
        except Exception as e:
            self.logger.error(f"Guide Sound menu not found: {str(e)}")
            return False