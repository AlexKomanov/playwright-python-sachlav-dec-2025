# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Playwright Python test automation framework for the Oasis Booking website. The framework uses pytest for test execution and Allure for reporting.

## Architecture and Structure

### Core Components
- **Pages**: Page Object Model implementation in the `pages/` directory
  - `base_page.py`: Base page class with common functionality
  - `main_page.py`: Handles main page interactions
  - `login_page.py`: Handles login functionality
  - `user_dashboard_page.py`: Handles user dashboard functionality after login
  - `property_search_page.py`: Handles property search and selection
  - `checkout_page.py`: Handles the complete checkout process
  - `demoqa_page.py`: Handles DemoQA website interactions
- **Tests**: Located in the `tests/` directory with different test scenarios
  - `test_success_login.py`: Tests successful login flow using page objects
  - `test_not_successful_login.py`: Tests failed login scenarios using page objects
  - `test_end_2_end.py`: Complete end-to-end booking flow using page objects
  - `demoqa/test_playwright_basics.py`: Tests for DemoQA website interactions using page objects
- **Utilities**: `utils/constants.py` contains environment variables and constants
- **Configuration**:
  - `pytest.ini`: Pytest configuration with browser settings and markers
  - `requirements.txt`: Project dependencies
  - `allurerc.json`: Allure report configuration

### Key Patterns
- Uses Playwright's sync API for browser automation
- Fully implements Page Object Model design pattern for all test scenarios
- Integrates Allure reporting with detailed steps and attachments
- Uses pytest fixtures for page objects initialization
- Environment variables managed through python-dotenv
- All page objects inherit from a common base class for consistency

### Private Access Modifiers
All page object classes use private attributes (prefixed with `__`) to encapsulate internal implementation details. Public access to locators is provided through properties when needed. This ensures proper encapsulation and prevents direct manipulation of internal elements.

Example:
```python
class LoginPage:
    def __init__(self, page: Page) -> None:
        self.__page = page
        self.__email_textfield = page.get_by_role("textbox", name="Email")
        self.__password_textfield = page.get_by_role("textbox", name="Password")
        self.__login_button = page.get_by_role("button", name="Login")

    @property
    def email_textfield(self) -> Locator:
        return self.__email_textfield

    def perform_login(self, email: str, password: str) -> None:
        self.__email_textfield.fill(email)  # Internal usage with private attribute
        self.__password_textfield.fill(password)
        self.__login_button.click()
```

## Common Development Commands

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_success_login.py

# Run tests with specific marker
pytest -m smoke

# Run tests in headed mode (to see browser)
pytest --headed
```

### Generating Allure Reports
```bash
# Generate and serve Allure report
allure serve allure-results

# Generate static report
allure generate allure-results -o allure-report
```

### Installing Dependencies
```bash
# Install project dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

## Test Configuration

The project is configured via `pytest.ini` with:
- Chromium browser by default
- Automatic screenshot, video, and tracing on failure
- Allure integration for detailed reporting
- Custom markers for test categorization (smoke, regression, login, checkout)

Environment variables are loaded from `.env` file using python-dotenv.

All tests now follow the Page Object Model pattern consistently, making them more maintainable and reusable.