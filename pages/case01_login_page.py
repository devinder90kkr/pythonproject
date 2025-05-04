from pages.base_page import BasePage
from utils.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators.USERNAME_FIELD))
        self.send_keys(self.locators.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.locators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.click(self.locators.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()