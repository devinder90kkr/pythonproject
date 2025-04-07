# Selenium Automation Framework

A robust and scalable Selenium WebDriver automation framework designed for web application testing. This framework follows best practices and provides comprehensive test reporting capabilities.

## Project Structure

```
seleniumautomation/
├── config/                      # Configuration files
│   ├── config.ini              # Environment and test configuration
│   └── test_data.json          # Test data and credentials
│
├── pages/                       # Page Object Model implementation
│   ├── base_page.py            # Base page with common functionality
│   ├── login_page.py           # Login page specific functionality
│   └── locators/               # Page element locators
│       └── login_locators.py   # Login page locators
│
├── tests/                       # Test suites
│   ├── test_login.py           # Login test cases
│   └── test_invalid_login.py   # Invalid login test cases
│
├── utils/                       # Utility classes
│   ├── driver_factory.py       # Browser driver initialization
│   ├── logger.py               # Logging utility
│   └── cleanup.py              # Report cleanup utility
│
├── reports/                     # Test reports and screenshots
│   ├── report.html             # HTML test report
│   └── screenshots/            # Test execution screenshots
│
├── logs/                        # Test execution logs
│   └── test_*.log              # Individual test logs
│
├── requirements.txt             # Python dependencies
├── pytest.ini                  # Pytest configuration
└── README.md                   # Project documentation
```

## Features

- **Page Object Model**: Clean and maintainable test structure
- **Multi-Browser Support**: Chrome, Firefox, Edge
- **Comprehensive Reporting**: 
  - HTML reports with screenshots
  - Detailed test logs
  - Screenshot capture on failure
- **Configurable Environment**: Easy setup for different environments
- **Data-Driven Testing**: Support for JSON test data
- **Automatic Cleanup**: Utility to manage old reports and logs

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Web browsers (Chrome, Firefox, Edge)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devinder90kkr/pythonproject.git
   cd seleniumautomation
   ```

2. Create and activate virtual environment:
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Update `config/config.ini`:
   ```ini
   [ENVIRONMENT]
   base_url = your_base_url
   
   [BROWSER]
   browser = chrome  # chrome, firefox, edge
   
   [TIMEOUTS]
   implicit_wait = 10
   explicit_wait = 30
   ```

2. Update `config/test_data.json`:
   ```json
   {
     "login": {
       "valid_username": "your_username",
       "valid_password": "your_password",
       "invalid_username": "invalid_user",
       "invalid_password": "invalid_pass"
     }
   }
   ```

## Running Tests

1. Run all tests:
   ```bash
   python -m pytest tests/ -v
   ```

2. Run specific test:
   ```bash
   python -m pytest tests/test_login.py -v
   ```

3. Generate HTML report:
   ```bash
   python -m pytest tests/ -v --html=reports/report.html --self-contained-html


   python -m pytest tests/test_dashboard.py -v --html=reports/report.html --self-contained-html --capture=no 
   ```

4. Run Test Suites:
   The framework provides different test suites that can be run using the `run_suites.py` script:

   ```bash
   python run_suites.py
   ```

   This will present a menu with the following options:
   - 1. Smoke Tests: Run all tests marked with `@pytest.mark.smoke`
   - 2. Regression Tests: Run all tests marked with `@pytest.mark.regression`
   - 3. Login Tests: Run all tests marked with `@pytest.mark.login`
   - 4. All Tests: Run all tests in the project

   Each suite generates its own HTML report:
   - Smoke Tests: `reports/smoke_report.html`
   - Regression Tests: `reports/regression_report.html`
   - Login Tests: `reports/login_report.html`
   - All Tests: `reports/full_report.html`

   You can also run specific suites directly using pytest:
   ```bash
   # Run smoke tests
   pytest -m smoke -v

   # Run regression tests
   pytest -m regression -v

   # Run login tests
   pytest -m login -v
   ```

   To mark tests for specific suites, use the following decorators in your test files:
   ```python
   @pytest.mark.smoke
   def test_smoke_feature():
       pass

   @pytest.mark.regression
   def test_regression_feature():
       pass

   @pytest.mark.login
   def test_login_feature():
       pass
   ```

## Reports and Logs

### Report Types
1. **HTML Reports**
   - Location: `reports/report.html`
   - Contains: Test execution summary, pass/fail status, test duration, error messages
   - View: Open in web browser

2. **Screenshots**
   - Location: `reports/screenshots/`
   - Captured for: Failed tests, login attempts, success scenarios
   - Format: PNG files with timestamp

3. **Log Files**
   - Location: `logs/`
   - Contains: Detailed step-by-step execution logs
   - Format: Text files with timestamp

### Cleaning Up Reports
```bash
# Remove reports older than 7 days (default)
python cleanup_reports.py

# Remove reports older than specific days
python cleanup_reports.py --days 14

# Remove all reports
python cleanup_reports.py --all

# start reports 
start reports\reports.html
```

## Best Practices

1. **Page Object Model**
   - Keep locators in page objects
   - Implement reusable methods
   - Use explicit waits

2. **Test Structure**
   - One test file per feature
   - Clear test names
   - Proper assertions

3. **Logging**
   - Log all important steps
   - Include error details
   - Use appropriate log levels

4. **Reporting**
   - Take screenshots on failure
   - Include detailed error messages
   - Clean up old reports regularly

## Troubleshooting

1. **Browser Issues**
   - Check browser version compatibility
   - Verify WebDriver version
   - Clear browser cache

2. **Test Failures**
   - Check logs in `logs/` directory
   - Review screenshots in `reports/screenshots/`
   - Verify test data in `config/test_data.json`

3. **Environment Issues**
   - Verify Python version
   - Check virtual environment
   - Update dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Contact

For any queries or support, please contact:
- Email: devinder90kkr@gmail.com 
- GitHub: [devinder90kkr](https://github.com/devinder90kkr) 