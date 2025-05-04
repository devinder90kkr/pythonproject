from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Input fields
    USERNAME_FIELD = (By.XPATH, "//input[@title='Username']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    # Buttons
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    

