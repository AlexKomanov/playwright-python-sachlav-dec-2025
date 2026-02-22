import allure
import pytest
from allure_commons.types import Severity
from pages.main_page import MainPage
from playwright.sync_api import Page, expect


@allure.epic("Oasis Booking")
@allure.feature("Booking Flow")
@allure.story("End to End Booking")
@allure.title("Complete booking flow from login to payment")
@allure.severity(Severity.BLOCKER)
@pytest.mark.regression
def test_example(page: Page) -> None:
    main_page = MainPage(page)

    with allure.step("Login to the application"):
        page.goto("https://stay-oasis-booking.lovable.app/")
        main_page.click_login_button()
        page.get_by_role("textbox", name="Email").click()
        page.get_by_role("textbox", name="Email").fill("john@example.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("password")
        page.get_by_role("button", name="Login").click()

    with allure.step("Verify user is logged in"):
        expect(page.get_by_test_id("user-menu-button")).to_be_visible()
        expect(page.locator("h1")).to_contain_text("Find your next dream stay")
        expect(page.get_by_test_id("user-menu-button")).to_contain_text("JD")

    with allure.step("Search and select a property"):
        page.get_by_role("button", name="Take me to the most").click()
        expect(page.get_by_test_id("book-now-btn")).to_be_visible()

    with allure.step("Adjust guest count"):
        page.get_by_test_id("increase-guest-btn").click()
        expect(page.get_by_role("main")).to_contain_text("2")

    with allure.step("Proceed to checkout"):
        page.get_by_test_id("book-now-btn").click()
        expect(page.get_by_role("heading", name="Checkout")).to_be_visible()

    with allure.step("Select facilities"):
        page.get_by_test_id("facility-checkbox-pool").click()
        page.get_by_test_id("facility-checkbox-gym").click()
        page.get_by_test_id("facility-checkbox-minibar").click()
        page.get_by_test_id("facility-spa").click()
        page.get_by_test_id("facility-airport").click()
        page.get_by_test_id("facilities-continue-btn").click()

    with allure.step("Select apartment type"):
        page.get_by_test_id("apartment-type-penthouse").click()
        page.get_by_test_id("apartment-type-continue-btn").click()

    with allure.step("Fill personal information"):
        page.get_by_test_id("personal-info-fullname").click()
        page.get_by_test_id("personal-info-fullname").press("ControlOrMeta+a")
        page.get_by_test_id("personal-info-fullname").fill("Alex Komanov")
        page.get_by_test_id("personal-info-email").click()
        page.get_by_test_id("personal-info-email").click()
        page.get_by_test_id("personal-info-email").dblclick()
        page.get_by_test_id("personal-info-email").press("ControlOrMeta+a")
        page.get_by_test_id("personal-info-email").fill("akomanovc88@gmail.com")
        page.get_by_test_id("personal-info-phone").click()
        page.get_by_test_id("personal-info-phone").click()
        page.get_by_test_id("personal-info-phone").dblclick()
        page.get_by_test_id("personal-info-phone").fill("0546998897")
        page.get_by_test_id("personal-info-special-requests").click()
        page.get_by_test_id("personal-info-special-requests").fill("need a quiet room")
        page.get_by_test_id("personal-info-continue-btn").click()

    with allure.step("Apply coupon"):
        page.get_by_role("button", name="Show available coupons").click()
        page.get_by_text("LUXURY50").click()
        page.get_by_role("button", name="Apply").click()
        expect(page.locator("#applied-coupon-code")).to_contain_text("LUXURY50 applied!")

    with allure.step("Complete payment"):
        page.get_by_test_id("pay-button").click()
        page.goto("https://stay-oasis-booking.lovable.app/")
