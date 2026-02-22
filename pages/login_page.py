import allure
from playwright.sync_api import Page, Locator


class LoginPage:

    page_title = "stay-oasis-booking"

    def __init__(self, page: Page) -> None:
        self.__page = page
        self.__email_textfield = page.get_by_role("textbox", name="Email")
        self.__password_textfield = page.get_by_role("textbox", name="Password")
        self.__login_button = page.get_by_role("button", name="Login")
        self.__error_element = page.get_by_role("alert")

    @allure.step("Perform login with email: {email}")
    def perform_login(self, email: str, password: str) -> None:
        self.__email_textfield.fill(email)
        self.__password_textfield.fill(password)
        self.__login_button.click()

    @property
    def error_element(self) -> Locator:
        return self.__error_element



