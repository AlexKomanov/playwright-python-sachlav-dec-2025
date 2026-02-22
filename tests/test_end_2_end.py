import allure
import pytest
from allure_commons.types import Severity
from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.user_dashboard_page import UserDashboardPage
from pages.property_search_page import PropertySearchPage
from pages.checkout_page import CheckoutPage


@allure.epic("Oasis Booking")
@allure.feature("Booking Flow")
@allure.story("End to End Booking")
@allure.title("Complete booking flow from login to payment")
@allure.severity(Severity.BLOCKER)
@pytest.mark.regression
def test_complete_booking_flow(page: Page) -> None:
    main_page = MainPage(page)
    login_page = LoginPage(page)
    dashboard_page = UserDashboardPage(page)
    property_search_page = PropertySearchPage(page)
    checkout_page = CheckoutPage(page)

    with allure.step("Login to the application"):
        main_page.open_page()
        main_page.click_login_button()
        login_page.perform_login("john@example.com", "password")

    with allure.step("Verify user is logged in"):
        dashboard_page.verify_user_logged_in("JD")

    with allure.step("Search and select a property"):
        property_search_page.click_take_me_button()
        property_search_page.verify_book_now_button_visible()

    with allure.step("Adjust guest count"):
        property_search_page.increase_guest_count()
        property_search_page.verify_guest_count("2")

    with allure.step("Proceed to checkout"):
        property_search_page.book_now_button.click()
        checkout_page.verify_checkout_page()

    with allure.step("Select facilities"):
        checkout_page.select_facilities()

    with allure.step("Select apartment type"):
        checkout_page.select_apartment_type()

    with allure.step("Fill personal information"):
        checkout_page.fill_personal_information(
            "Alex Komanov",
            "akomanovc88@gmail.com",
            "0546998897",
            "need a quiet room"
        )

    with allure.step("Apply coupon"):
        checkout_page.apply_coupon()
        checkout_page.verify_coupon_applied("LUXURY50")

    with allure.step("Complete payment"):
        checkout_page.complete_payment()
        main_page.open_page()