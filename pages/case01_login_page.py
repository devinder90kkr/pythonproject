from pages.base_page import BasePage
from utils.locators import LoginPageLocators
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

    def login(self, username, password):
        self.logger.info("Starting login process")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.take_screenshot("login_attempt")
        self.logger.info("Login process completed")