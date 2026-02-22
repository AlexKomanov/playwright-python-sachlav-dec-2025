import allure
from allure_commons.types import Severity
from playwright.sync_api import Page
from pages.demoqa_page import DemoQAPage, DemoQATextBoxPage


@allure.epic("Oasis Booking")
@allure.feature("Playwright Basics")
@allure.story("DemoQA Interactions")
@allure.title("Verify button click and double click actions")
@allure.severity(Severity.MINOR)
def test_demoqa_button_interactions(page: Page):
    demoqa_page = DemoQAPage(page)

    with allure.step("Navigate to buttons page"):
        demoqa_page.navigate_to_buttons()

    with allure.step("Perform single click"):
        demoqa_page.click_button()

    with allure.step("Perform double click"):
        demoqa_page.double_click_button()

    with allure.step("Verify click results"):
        demoqa_page.verify_click_results()

    with allure.step("Wait for stability"):
        page.wait_for_timeout(3000)


@allure.epic("Oasis Booking")
@allure.feature("Playwright Basics")
@allure.story("DemoQA Interactions")
@allure.title("Verify text box form submission")
@allure.severity(Severity.MINOR)
def test_demoqa_textbox_submission(page: Page):
    textbox_page = DemoQATextBoxPage(page)
    full_name = "Alex Komanov"
    email = "akomanov@gmail.com"

    with allure.step("Navigate to text box page"):
        textbox_page.navigate_to_text_box()

    with allure.step("Fill in the form"):
        textbox_page.fill_form(full_name, email)

    with allure.step("Submit the form"):
        textbox_page.submit_form()

    with allure.step("Verify submitted data"):
        textbox_page.verify_submitted_data(full_name, email)