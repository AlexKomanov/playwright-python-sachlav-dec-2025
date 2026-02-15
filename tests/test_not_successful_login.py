from playwright.sync_api import Page, expect
from utils import constants
import pytest

@pytest.mark.regression
def test_example(page: Page, main_page, login_page) -> None:
    main_page.open_page()
    main_page.click_login_button()
    login_page.perform_login(constants.GUEST_EMAIL, constants.INCORRECT_PASSWORD)

    expect(login_page.error_element).to_contain_text(constants.LOGIN_ERROR_MESSAGE)
    expect(page).to_have_url(constants.LOGIN_URL)
    expect(page).to_have_title(login_page.page_title)
