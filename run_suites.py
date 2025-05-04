import pytest
import os
import sys

def run_test_suite():
    """
    Run the test suite for login test cases
    """
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define test files to run
    test_files = [
        os.path.join(current_dir, 'tests', 'case01_test_login.py'),
        os.path.join(current_dir, 'tests', 'case02_test_invalid_login.py')
    ]
    
    # Run the tests
    pytest.main([
        '-v',  # verbose output
        *test_files
    ])

if __name__ == '__main__':
    run_test_suite() 