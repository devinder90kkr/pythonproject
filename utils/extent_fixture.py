import pytest
from .extent_report_manager import ExtentReportManager
import os
from datetime import datetime

@pytest.fixture(scope="session", autouse=True)
def extent_report():
    """
    Fixture to initialize and manage Extent Reports for the test session
    """
    # Get the ExtentReportManager instance
    report_manager = ExtentReportManager.get_instance()
    
    yield report_manager
    
    # After all tests are complete, flush the report
    report_manager.flush_report()

@pytest.fixture(autouse=True)
def test_logger(request, extent_report):
    """
    Fixture to log test information to Extent Reports
    """
    # Start the test in the report
    test_name = request.node.name
    test_description = request.node.function.__doc__ or ""
    extent_report.start_test(test_name, test_description)
    
    yield
    
    # End the test in the report
    extent_report.end_test()

def pytest_exception_interact(node, call, report):
    """
    Hook to handle test failures and log them to Extent Reports
    """
    if report.failed:
        report_manager = ExtentReportManager.get_instance()
        
        # Log the failure
        failure_message = str(report.longrepr)
        report_manager.log_fail(f"Test Failed: {failure_message}")
        
        # Take screenshot if the test has a driver fixture
        if hasattr(node, 'funcargs') and 'driver' in node.funcargs:
            driver = node.funcargs['driver']
            try:
                # Create screenshots directory if it doesn't exist
                if not os.path.exists("reports/screenshots"):
                    os.makedirs("reports/screenshots")
                
                # Take screenshot
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = f"reports/screenshots/{node.name}_{timestamp}.png"
                driver.save_screenshot(screenshot_path)
                
                # Add screenshot to report
                report_manager.add_screenshot(screenshot_path, "Test Failure Screenshot")
            except Exception as e:
                report_manager.log_warning(f"Failed to capture screenshot: {str(e)}") 