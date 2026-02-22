import allure
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        # Facilities selection
        self.__facility_pool_checkbox = page.get_by_test_id("facility-checkbox-pool")
        self.__facility_gym_checkbox = page.get_by_test_id("facility-checkbox-gym")
        self.__facility_minibar_checkbox = page.get_by_test_id("facility-checkbox-minibar")
        self.__facility_spa_checkbox = page.get_by_test_id("facility-spa")
        self.__facility_airport_checkbox = page.get_by_test_id("facility-airport")
        self.__facilities_continue_button = page.get_by_test_id("facilities-continue-btn")

        # Apartment type selection
        self.__apartment_penthouse = page.get_by_test_id("apartment-type-penthouse")
        self.__apartment_continue_button = page.get_by_test_id("apartment-type-continue-btn")

        # Personal info
        self.__personal_fullname = page.get_by_test_id("personal-info-fullname")
        self.__personal_email = page.get_by_test_id("personal-info-email")
        self.__personal_phone = page.get_by_test_id("personal-info-phone")
        self.__personal_special_requests = page.get_by_test_id("personal-info-special-requests")
        self.__personal_continue_button = page.get_by_test_id("personal-info-continue-btn")

        # Coupon
        self.__show_coupons_button = page.get_by_role("button", name="Show available coupons")
        self.__coupon_luxury50 = page.get_by_text("LUXURY50")
        self.__apply_coupon_button = page.get_by_role("button", name="Apply")
        self.__applied_coupon_message = page.locator("#applied-coupon-code")

        # Payment
        self.__pay_button = page.get_by_test_id("pay-button")

        # Checkout heading
        self.__checkout_heading = page.get_by_role("heading", name="Checkout")

    @allure.step("Verify checkout page is loaded")
    def verify_checkout_page(self) -> None:
        self.__checkout_heading.wait_for(state="visible")

    @allure.step("Select facilities")
    def select_facilities(self) -> None:
        self.__facility_pool_checkbox.click()
        self.__facility_gym_checkbox.click()
        self.__facility_minibar_checkbox.click()
        self.__facility_spa_checkbox.click()
        self.__facility_airport_checkbox.click()
        self.__facilities_continue_button.click()

    @allure.step("Select apartment type")
    def select_apartment_type(self) -> None:
        self.__apartment_penthouse.click()
        self.__apartment_continue_button.click()

    @allure.step("Fill personal information")
    def fill_personal_information(self, fullname: str, email: str, phone: str, special_requests: str) -> None:
        self.__personal_fullname.click()
        self.__personal_fullname.press("ControlOrMeta+a")
        self.__personal_fullname.fill(fullname)

        self.__personal_email.click()
        self.__personal_email.dblclick()
        self.__personal_email.press("ControlOrMeta+a")
        self.__personal_email.fill(email)

        self.__personal_phone.click()
        self.__personal_phone.dblclick()
        self.__personal_phone.fill(phone)

        self.__personal_special_requests.click()
        self.__personal_special_requests.fill(special_requests)

        self.__personal_continue_button.click()

    @allure.step("Apply coupon")
    def apply_coupon(self, coupon_code: str = "LUXURY50") -> None:
        self.__show_coupons_button.click()
        self.__coupon_luxury50.click()
        self.__apply_coupon_button.click()

    @allure.step("Verify coupon is applied")
    def verify_coupon_applied(self, coupon_code: str) -> None:
        self.__applied_coupon_message.filter(has_text=f"{coupon_code} applied!").wait_for(state="visible")

    @allure.step("Complete payment")
    def complete_payment(self) -> None:
        self.__pay_button.click()

    # Properties for private attributes
    @property
    def facility_pool_checkbox(self) -> Locator:
        return self.__facility_pool_checkbox

    @property
    def facility_gym_checkbox(self) -> Locator:
        return self.__facility_gym_checkbox

    @property
    def facility_minibar_checkbox(self) -> Locator:
        return self.__facility_minibar_checkbox

    @property
    def facility_spa_checkbox(self) -> Locator:
        return self.__facility_spa_checkbox

    @property
    def facility_airport_checkbox(self) -> Locator:
        return self.__facility_airport_checkbox

    @property
    def facilities_continue_button(self) -> Locator:
        return self.__facilities_continue_button

    @property
    def apartment_penthouse(self) -> Locator:
        return self.__apartment_penthouse

    @property
    def apartment_continue_button(self) -> Locator:
        return self.__apartment_continue_button

    @property
    def personal_fullname(self) -> Locator:
        return self.__personal_fullname

    @property
    def personal_email(self) -> Locator:
        return self.__personal_email

    @property
    def personal_phone(self) -> Locator:
        return self.__personal_phone

    @property
    def personal_special_requests(self) -> Locator:
        return self.__personal_special_requests

    @property
    def personal_continue_button(self) -> Locator:
        return self.__personal_continue_button

    @property
    def show_coupons_button(self) -> Locator:
        return self.__show_coupons_button

    @property
    def coupon_luxury50(self) -> Locator:
        return self.__coupon_luxury50

    @property
    def apply_coupon_button(self) -> Locator:
        return self.__apply_coupon_button

    @property
    def applied_coupon_message(self) -> Locator:
        return self.__applied_coupon_message

    @property
    def pay_button(self) -> Locator:
        return self.__pay_button

    @property
    def checkout_heading(self) -> Locator:
        return self.__checkout_heading