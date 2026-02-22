import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page, expect


@allure.epic("Oasis Booking")
@allure.feature("Authentication")
@allure.story("Successful Login")
@allure.title("Verify successful login with valid credentials")
@allure.severity(Severity.CRITICAL)
@pytest.mark.regression
def test_example(page: Page) -> None:
    with allure.step("Navigate to main page"):
        page.goto("https://stay-oasis-booking.lovable.app/")

    with allure.step("Open login form"):
        page.get_by_role("button", name="Login").click()

    with allure.step("Fill in login credentials"):
        page.get_by_role("textbox", name="Email").click()
        page.get_by_role("textbox", name="Email").fill("jane@example.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("password")

    with allure.step("Submit login form"):
        page.get_by_role("button", name="Login").click()

    with allure.step("Verify user is logged in"):
        expect(page.get_by_test_id("user-menu-button")).to_be_visible()
