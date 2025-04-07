from pages.base_page import BasePage
from pages.locators.login_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import Logger
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
        self.logger = Logger()  # Initialize logger

    def enter_username(self, username):
        self.logger.info(f"Waiting for username field to be visible")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators.USERNAME_FIELD))
        self.logger.info(f"Entering username: {username}")
        self.send_keys(self.locators.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.send_keys(self.locators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.logger.info("Clicking login button")
        self.click(self.locators.LOGIN_BUTTON)
        
    def is_staff_details_present(self):
        try:
            wait = WebDriverWait(self.driver, 3000)
            staff_details = wait.until(EC.presence_of_element_located(self.locators.STAFF_DETAILS))
            self.logger.info(f"Staff details found: {staff_details.text}")
            return True
        except Exception as e:
            self.logger.error(f"Staff details not found: {str(e)}")
            return False

    def is_error_message_present(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            error_message = wait.until(EC.presence_of_element_located(self.locators.ERROR_MESSAGE))
            self.logger.info(f"Error message found: {error_message.text}")
            return True
        except Exception as e:
            self.logger.error(f"Error message not found: {str(e)}")
            return False

    def login(self, username, password):
        self.logger.info("Starting login process")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.take_screenshot("login_attempt")
        
        # Wait for either success or error message
        if self.is_staff_details_present():
            self.logger.info("Login successful - Staff details found")
            return True
        elif self.is_error_message_present():
            self.logger.info("Login failed - Error message found")
            return False
        else:
            self.logger.error("Neither success nor error message found")
            return False