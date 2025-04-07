import pytest
from datetime import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Get the driver from the test instance
            driver = getattr(item.cls, 'driver', None)
            if driver is not None:
                # Create screenshots directory if it doesn't exist
                screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'screenshots')
                if not os.path.exists(screenshots_dir):
                    os.makedirs(screenshots_dir)
                
                # Take screenshot
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                screenshot_path = os.path.join(screenshots_dir, f'screenshot_{timestamp}.png')
                driver.save_screenshot(screenshot_path)
                
                # Add screenshot to report
                extra.append(pytest_html.extras.image(screenshot_path))
        
        report.extra = extra

@pytest.fixture(scope="function", autouse=True)
def setup_teardown(request):
    """
    Setup and teardown for each test
    """
    yield
    # Take screenshot after each test
    driver = getattr(request.cls, 'driver', None)
    if driver is not None:
        # Create screenshots directory if it doesn't exist
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports', 'screenshots')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        # Take screenshot
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join(screenshots_dir, f'test_{request.node.name}_{timestamp}.png')
        driver.save_screenshot(screenshot_path) 