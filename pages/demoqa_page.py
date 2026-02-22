import allure
from playwright.sync_api import Page, Locator, expect
from pages.base_page import BasePage


class DemoQAPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__buttons_click_me = page.get_by_role("button", name="Click Me", exact=True)
        self.__buttons_double_click = page.locator('[id="doubleClickBtn"]')
        self.__double_click_message = page.locator('#doubleClickMessage')
        self.__dynamic_click_message = page.locator('#dynamicClickMessage')

    @allure.step("Navigate to buttons page")
    def navigate_to_buttons(self) -> None:
        self.goto("https://demoqa.com/buttons")

    @allure.step("Perform single click")
    def click_button(self) -> None:
        self.__buttons_click_me.click(timeout=10000)

    @allure.step("Perform double click")
    def double_click_button(self) -> None:
        self.__buttons_double_click.dblclick()

    @allure.step("Verify click results")
    def verify_click_results(self) -> None:
        expect(self.__double_click_message).to_have_text("You have done a double click")
        expect(self.__dynamic_click_message).to_contain_text("You have done a dynamic click")

    # Properties for private attributes
    @property
    def buttons_click_me(self) -> Locator:
        return self.__buttons_click_me

    @property
    def buttons_double_click(self) -> Locator:
        return self.__buttons_double_click

    @property
    def double_click_message(self) -> Locator:
        return self.__double_click_message

    @property
    def dynamic_click_message(self) -> Locator:
        return self.__dynamic_click_message


class DemoQATextBoxPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.__full_name_input = page.get_by_placeholder("Full Name")
        self.__email_input = page.locator("#userEmail")
        self.__submit_button = page.get_by_role("button", name="Submit", exact=True)
        self.__name_result = page.locator('[id="name"]')
        self.__email_result = page.locator('[id="email"]')

    @allure.step("Navigate to text box page")
    def navigate_to_text_box(self) -> None:
        self.goto("https://demoqa.com/text-box")

    @allure.step("Fill in the form with name: {full_name} and email: {email}")
    def fill_form(self, full_name: str, email: str) -> None:
        self.__full_name_input.fill(full_name)
        self.__email_input.press_sequentially(email, delay=150)

    @allure.step("Submit the form")
    def submit_form(self) -> None:
        self.__submit_button.click(timeout=10000)

    @allure.step("Verify submitted data")
    def verify_submitted_data(self, full_name: str, email: str) -> None:
        expect(self.__name_result).to_have_text(f"Name:{full_name}")
        expect(self.__email_result).to_have_text(f"Email:{email}")

    # Properties for private attributes
    @property
    def full_name_input(self) -> Locator:
        return self.__full_name_input

    @property
    def email_input(self) -> Locator:
        return self.__email_input

    @property
    def submit_button(self) -> Locator:
        return self.__submit_button

    @property
    def name_result(self) -> Locator:
        return self.__name_result

    @property
    def email_result(self) -> Locator:
        return self.__email_result