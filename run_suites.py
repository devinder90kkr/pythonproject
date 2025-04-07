import pytest
import os
import sys
from datetime import datetime

def run_smoke_tests():
    """Run all smoke tests"""
    print("\nRunning Smoke Tests...")
    pytest.main([
        "-m", "smoke",
        "-v",
        "--html=reports/smoke_report.html",
        "--self-contained-html"
    ])

def run_regression_tests():
    """Run all regression tests"""
    print("\nRunning Regression Tests...")
    pytest.main([
        "-m", "regression",
        "-v",
        "--html=reports/regression_report.html",
        "--self-contained-html"
    ])

def run_login_tests():
    """Run all login-related tests"""
    print("\nRunning Login Tests...")
    pytest.main([
        "-m", "login",
        "-v",
        "--html=reports/login_report.html",
        "--self-contained-html"
    ])

def run_all_tests():
    """Run all tests"""
    print("\nRunning All Tests...")
    pytest.main([
        "-v",
        "--html=reports/full_report.html",
        "--self-contained-html"
    ])

if __name__ == "__main__":
    # Create reports directory if it doesn't exist
    if not os.path.exists("reports"):
        os.makedirs("reports")
    
    # Get current timestamp for report naming
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    print("Select test suite to run:")
    print("1. Smoke Tests")
    print("2. Regression Tests")
    print("3. Login Tests")
    print("4. All Tests")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        run_smoke_tests()
    elif choice == "2":
        run_regression_tests()
    elif choice == "3":
        run_login_tests()
    elif choice == "4":
        run_all_tests()
    else:
        print("Invalid choice. Please select a number between 1 and 4.") 