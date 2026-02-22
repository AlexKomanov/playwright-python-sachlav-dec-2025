import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_dashboard_page import UserDashboardPage


@allure.epic("Oasis Booking")
@allure.feature("Authentication")
@allure.story("Successful Login")
@allure.title("Verify successful login with valid credentials")
@allure.severity(Severity.CRITICAL)
@pytest.mark.regression
def test_successful_login(page: Page) -> None:
    main_page = MainPage(page)
    login_page = LoginPage(page)
    dashboard_page = UserDashboardPage(page)

    with allure.step("Navigate to main page"):
        main_page.open_page()

    with allure.step("Open login form"):
        main_page.click_login_button()

    with allure.step("Fill in login credentials"):
        login_page.perform_login("jane@example.com", "password")

    with allure.step("Verify user is logged in"):
        dashboard_page.verify_user_logged_in("JD")