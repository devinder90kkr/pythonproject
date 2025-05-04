import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from utils.driver_factory import DriverFactory
from pages.base_page import BasePage
from configparser import ConfigParser
import json

def load_config():
    config = ConfigParser()
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
    config.read(config_path)
    return config

def load_test_data():
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'test_data.json'), 'r') as f:
        return json.load(f)

@pytest.fixture(scope="class")
def setup(request):
    """
    Setup fixture that initializes the driver and other components
    """
    driver = DriverFactory().get_driver()
    base_page = BasePage(driver)
    
    # Store in request context
    request.cls.driver = driver
    request.cls.base_page = base_page
    request.cls.config = load_config()
    request.cls.test_data = load_test_data()
    
    yield
    
    # Teardown
    driver.quit() 