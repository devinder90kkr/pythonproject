from datetime import datetime
import os
import pytest
import webbrowser

class ExtentReportManager:
    _instance = None
    _test = None
    _report_path = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ExtentReportManager()
        return cls._instance

    def __init__(self):
        if ExtentReportManager._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ExtentReportManager._instance = self
            self._setup_reports()

    def _setup_reports(self):
        if not os.path.exists("reports"):
            os.makedirs("reports")
        
        # Create a unique report name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self._report_path = f"reports/extent_report_{timestamp}.html"

    def start_test(self, test_name, description=""):
        """Start a new test in the report"""
        self._test = test_name
        return self._test

    def end_test(self):
        """End the current test"""
        pass

    def flush_report(self):
        """Save and close the report"""
        if self._report_path:
            # Open the report in the default web browser
            webbrowser.open('file://' + os.path.realpath(self._report_path))

    def log_info(self, message):
        """Log an info message"""
        pytest.attach(message, "INFO", pytest.html)

    def log_pass(self, message):
        """Log a pass message"""
        pytest.attach(message, "PASS", pytest.html)

    def log_fail(self, message):
        """Log a fail message"""
        pytest.attach(message, "FAIL", pytest.html)

    def log_skip(self, message):
        """Log a skip message"""
        pytest.attach(message, "SKIP", pytest.html)

    def log_warning(self, message):
        """Log a warning message"""
        pytest.attach(message, "WARNING", pytest.html)

    def add_screenshot(self, screenshot_path, title=""):
        """Add a screenshot to the report"""
        pytest.attach.file(screenshot_path, name=title, attachment_type=pytest.html) 