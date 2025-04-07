import pytest
import os
from datetime import datetime
from pathlib import Path
import pytest_html

def pytest_configure(config):
    """
    Configure pytest to generate HTML reports
    """
    # Create reports directory if it doesn't exist
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)
    
    # Create screenshots directory if it doesn't exist
    screenshots_dir = Path("reports/screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    
    # Configure HTML report
    if not hasattr(config, 'workerinput'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        config.option.htmlpath = f"reports/report_{timestamp}.html"

def pytest_html_report_title(report):
    """
    Set the title of the HTML report
    """
    report.title = "Test Automation Report"

def pytest_html_results_table_header(cells):
    """
    Customize the HTML report table header
    """
    cells.insert(2, pytest_html.table_header("Description"))
    cells.insert(1, pytest_html.table_header("Time"))
    cells.pop()

def pytest_html_results_table_row(report, cells):
    """
    Customize the HTML report table row
    """
    cells.insert(2, pytest_html.table_cell(report.description))
    cells.insert(1, pytest_html.table_cell(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    cells.pop()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Add screenshot to HTML report on test failure
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        # Get the test class instance
        test_instance = item.instance
        if hasattr(test_instance, 'driver'):
            # Take screenshot
            screenshot_path = f"reports/screenshots/{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            test_instance.driver.save_screenshot(screenshot_path)
            
            # Add screenshot to report
            if hasattr(report, 'extra'):
                report.extra.append(pytest_html.extras.image(screenshot_path)) 