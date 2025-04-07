# Selenium Automation Framework

This is a Python-based Selenium WebDriver automation framework designed for web application testing.

## Features

- Page Object Model implementation
- Support for multiple browsers (Chrome, Firefox, Edge)
- Configurable test environment
- Detailed logging
- Screenshot capture on test failure
- HTML test reports
- Parallel test execution
- Data-driven testing support

## Project Structure

```
seleniumautomation/
├── config/
│   ├── config.ini        # Configuration settings
│   └── test_data.json    # Test data
├── pages/
│   └── base_page.py      # Base page object
├── tests/
│   └── test_suite.py     # Test cases
├── utils/
│   ├── driver_factory.py # Browser initialization
│   ├── logger.py         # Logging utility
│   └── helpers.py        # Helper functions
├── reports/              # Test reports and screenshots
├── requirements.txt      # Python dependencies
└── README.md            # Documentation
```

## Setup

1. Install Python 3.8 or higher
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Update `config/config.ini` with your environment settings:
   - Base URL
   - Browser selection
   - Timeouts
   - Report paths

2. Add test data to `config/test_data.json`

## Running Tests

Run all tests:
```bash
pytest tests/
```

Run specific test:
```bash
pytest tests/test_login.py
but working below command
python -m pytest tests/test_login.py -v
```

Run tests in parallel:
```bash
pytest -n auto tests/
```

### Generating Test Reports

1. **Generate HTML Report with Screenshots**:
   ```bash
   python -m pytest tests/ -v --html=reports/report.html --self-contained-html
   ```

2. **Generate Detailed HTML Report with Screenshots and Logs**:
   ```bash
   python -m pytest tests/ -v --html=reports/report.html --self-contained-html --capture=tee-sys
   ```

3. **Generate Report for Specific Test**:
   ```bash
   python -m pytest tests/test_login.py -v --html=reports/login_report.html --self-contained-html
   ```

4. **View Generated Reports**:
   ```bash
   # On Windows
   start reports\report.html
   
   # On Linux/Mac
   open reports/report.html
   ```

### Report Generation Options

1. **Basic Report**:
   - Test execution summary
   - Pass/fail status
   - Test duration
   - Error messages

2. **Detailed Report** (add `--capture=tee-sys`):
   - All basic report features
   - Console output
   - System logs
   - Test execution logs

3. **Report with Screenshots**:
   - All test reports include screenshots
   - Screenshots are stored in `reports/screenshots/`
   - Automatically captured for:
     - Failed tests
     - Login attempts
     - Success scenarios

4. **Log Files**:
   - Location: `logs/`
   - Format: Text files with timestamp
   - Contains detailed execution logs

### Viewing Reports

1. **HTML Report**:
   - Open `reports/report.html` in any web browser
   - View test execution summary
   - Check pass/fail status
   - Review error messages
   - View attached screenshots

2. **Log Files**:
   - Open log files in `logs/` directory
   - View detailed execution steps
   - Check error messages
   - Review test timing

3. **Screenshots**:
   - View screenshots in `reports/screenshots/`
   - Screenshots are named with timestamp
   - Includes both success and failure scenarios

## Reports and Logs Management

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

### Cleaning Up Reports and Logs

The framework provides utilities to manage report and log files:

1. **Remove reports older than X days** (default: 7 days):
   ```bash
   python cleanup_reports.py
   ```

2. **Remove reports older than specific number of days**:
   ```bash
   python cleanup_reports.py --days 14
   ```

3. **Remove all reports and logs**:
   ```bash
   python cleanup_reports.py --all
   ```

### Report Contents
- Test execution summary
- Pass/fail status for each test
- Test duration
- Error messages and stack traces
- Screenshots of failed tests
- Detailed step-by-step logs

### Log Contents
- Test start/end times
- Browser actions
- Page interactions
- Error messages
- Screenshot capture events
- Test assertions

## Best Practices

1. Use Page Object Model for all web pages
2. Keep locators in page objects
3. Use explicit waits instead of implicit waits
4. Add proper logging for test steps
5. Handle test data through JSON files
6. Take screenshots on test failure
7. Use meaningful test names and descriptions

## Troubleshooting

1. Check browser compatibility
2. Verify network connectivity
3. Review logs in the logs directory
4. Check screenshots for failed tests
5. Ensure all dependencies are installed

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 