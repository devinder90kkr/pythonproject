# Selenium Automation Framework

A robust and scalable Selenium WebDriver automation framework designed for web application testing. This framework follows best practices and provides a clean, maintainable structure for test automation.

## Project Structure

```
seleniumautomation/
├── config/                      # Configuration files
│   ├── config.ini              # Environment and test configuration
│   └── test_data.json          # Test data and credentials
│
├── pages/                       # Page Object Model implementation
│   ├── base_page.py            # Base page with common functionality
│   └── case01_login_page.py    # Login page specific functionality
│
├── tests/                       # Test suites
│   ├── case01_test_login.py    # Valid login test cases
│   └── case02_test_invalid_login.py  # Invalid login test cases
│
├── utils/                       # Utility classes
│   ├── driver_factory.py       # Browser driver initialization
│   └── locators.py             # Page element locators
│
├── requirements.txt             # Python dependencies
├── run_suites.py               # Test suite runner
└── README.md                   # Project documentation
```

## Features

- **Page Object Model**: Clean and maintainable test structure
- **Multi-Browser Support**: Chrome, Firefox, Edge
- **Configurable Environment**: Easy setup for different environments
- **Data-Driven Testing**: Support for JSON test data

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
   python -m pytest tests/case01_test_login.py -v
   ```

3. Run Test Suites:
   The framework provides a test suite runner that can be executed using the `run_suites.py` script:

   ```bash
   python run_suites.py
   ```

   This will run both login test cases:
   - Valid login tests (case01)
   - Invalid login tests (case02)

## Best Practices

1. **Page Object Model**
   - Keep locators in utils/locators.py
   - Implement reusable methods in base_page.py
   - Use explicit waits for better reliability

2. **Test Structure**
   - One test file per feature
   - Clear test names
   - Proper assertions

3. **Test Organization**
   - Group related tests together
   - Use meaningful test case names
   - Follow consistent naming conventions

## Troubleshooting

1. **Browser Issues**
   - Check browser version compatibility
   - Verify WebDriver version
   - Clear browser cache

2. **Test Failures**
   - Check test data in `config/test_data.json`
   - Verify environment configuration
   - Review test assertions

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