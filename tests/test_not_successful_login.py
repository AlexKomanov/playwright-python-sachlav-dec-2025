import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page, expect
from utils import constants


@allure.epic("Oasis Booking")
@allure.feature("Authentication")
@allure.story("Unsuccessful Login")
@allure.title("Verify error message on login with invalid credentials")
@allure.severity(Severity.CRITICAL)
@pytest.mark.regression
def test_example(page: Page, main_page, login_page) -> None:
    main_page.open_page()
    main_page.click_login_button()
    login_page.perform_login(constants.GUEST_EMAIL, constants.INCORRECT_PASSWORD)

    with allure.step("Verify error message is displayed"):
        expect(login_page.error_element).to_contain_text(constants.LOGIN_ERROR_MESSAGE)

    with allure.step("Verify URL remains on login page"):
        expect(page).to_have_url(constants.LOGIN_URL)

    with allure.step("Verify page title"):
        expect(page).to_have_title(login_page.page_title)
