import allure
from allure_commons.types import Severity
from playwright.sync_api import Page, expect


@allure.epic("Oasis Booking")
@allure.feature("Playwright Basics")
@allure.story("DemoQA Interactions")
@allure.title("Verify button click and double click actions")
@allure.severity(Severity.MINOR)
def test_playwright_basic_test_1(page: Page):
    with allure.step("Navigate to buttons page"):
        page.goto("https://demoqa.com/buttons")

    with allure.step("Perform single click"):
        page.get_by_role("button", name="Click Me", exact=True).click(timeout=10000)

    with allure.step("Perform double click"):
        page.locator('[id="doubleClickBtn"]').dblclick()

    with allure.step("Verify click results"):
        expect(page.locator('#doubleClickMessage')).to_have_text("You have done a double click")
        expect(page.locator('#dynamicClickMessage')).to_contain_text("You have done a dynamic click")

    page.wait_for_timeout(3000)


@allure.epic("Oasis Booking")
@allure.feature("Playwright Basics")
@allure.story("DemoQA Interactions")
@allure.title("Verify text box form submission")
@allure.severity(Severity.MINOR)
def test_playwright_basic_test_2(page: Page):
    full_name = "Alex Komanov"
    email = "akomanov@gmail.com"

    with allure.step("Navigate to text box page"):
        page.goto("https://demoqa.com/text-box")

    with allure.step("Fill in the form"):
        page.get_by_placeholder("Full Name").fill(full_name)
        page.wait_for_timeout(1000)
        page.locator("#userEmail").press_sequentially(email, delay=150)

    with allure.step("Submit the form"):
        page.get_by_role("button", name="Submit", exact=True).click(timeout=10000)

    with allure.step("Verify submitted data"):
        expect(page.locator('[id="name"]')).to_have_text(f"Name:{full_name}")
        expect(page.locator('[id="email"]')).to_have_text(f"Email:{email}")
