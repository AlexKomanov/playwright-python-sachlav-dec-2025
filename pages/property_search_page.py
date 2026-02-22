import allure
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class PropertySearchPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__take_me_button = page.get_by_role("button", name="Take me to the most")
        self.__book_now_button = page.get_by_test_id("book-now-btn")
        self.__increase_guest_button = page.get_by_test_id("increase-guest-btn")
        self.__guest_count_display = page.get_by_role("main")

    @allure.step("Click 'Take me to the most' button")
    def click_take_me_button(self) -> None:
        self.__take_me_button.click()

    @allure.step("Verify book now button is visible")
    def verify_book_now_button_visible(self) -> None:
        self.__book_now_button.wait_for(state="visible")

    @allure.step("Increase guest count")
    def increase_guest_count(self) -> None:
        self.__increase_guest_button.click()

    @allure.step("Verify guest count is updated to {count}")
    def verify_guest_count(self, count: str) -> None:
        self.__guest_count_display.filter(has_text=count).wait_for(state="visible")

    @property
    def take_me_button(self) -> Locator:
        return self.__take_me_button

    @property
    def book_now_button(self) -> Locator:
        return self.__book_now_button

    @property
    def increase_guest_button(self) -> Locator:
        return self.__increase_guest_button

    @property
    def guest_count_display(self) -> Locator:
        return self.__guest_count_display