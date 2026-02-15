import pytest
from playwright.sync_api import Page, expect

@pytest.mark.regression
def test_example(page: Page) -> None:
    page.goto("https://stay-oasis-booking.lovable.app/")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("jane@example.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_test_id("user-menu-button")).to_be_visible()
