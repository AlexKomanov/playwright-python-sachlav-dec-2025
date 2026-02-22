import allure
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class UserDashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__user_menu_button = page.get_by_test_id("user-menu-button")
        self.__page_heading = page.locator("h1")

    @allure.step("Verify user is logged in")
    def verify_user_logged_in(self, user_initials: str = "JD") -> None:
        self.__user_menu_button.wait_for(state="visible")
        self.__user_menu_button.filter(has_text=user_initials).wait_for(state="visible")
        self.__page_heading.filter(has_text="Find your next dream stay").wait_for(state="visible")

    @property
    def user_menu_button(self) -> Locator:
        return self.__user_menu_button

    @property
    def page_heading(self) -> Locator:
        return self.__page_heading