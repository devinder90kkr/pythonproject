from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Input fields
    USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
    
    # Buttons
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    
    # Staff details
    STAFF_DETAILS = (By.XPATH, "//h6[normalize-space()='Jordan - Wellness Advocate']")

    # Dashboard Locators
    SCHEDULE_MASTER = (By.XPATH, "//li[@id='schedule-master']")
    MEMBER_COMMUNICATION = (By.XPATH, "//li[@id='member-communication']")
    MEMBER_SUMMARY = (By.XPATH, "//li[@id='member-summary']")
    MEMBER_CALL = (By.XPATH, "//li[@id='member-calls']")
    GUIDE_SOUND = (By.XPATH, "//li[@id='breathe-sound']")

