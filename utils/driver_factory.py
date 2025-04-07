from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configparser import ConfigParser
import os

class DriverFactory:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini'))

    def get_driver(self):
        browser = self.config.get('ENVIRONMENT', 'browser').lower()
        headless = self.config.getboolean('ENVIRONMENT', 'headless')

        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.maximize_window()
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('--headless')
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        elif browser == 'edge':
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless')
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        # Set timeouts
        driver.implicitly_wait(int(self.config.get('TIMEOUTS', 'implicit_wait')))
        driver.set_page_load_timeout(int(self.config.get('TIMEOUTS', 'page_load_timeout')))

        return driver 