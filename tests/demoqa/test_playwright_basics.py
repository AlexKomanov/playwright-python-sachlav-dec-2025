from playwright.sync_api import Page, expect


def test_playwright_basic_test_1(page: Page):
    page.goto("https://demoqa.com/buttons")
    # page.get_by_role("button", name="Click Me").nth(2).click() # nth()
    # page.get_by_role("button", name="Click Me").last.click() # last
    page.get_by_role("button", name="Click Me", exact=True).click(timeout=10000)
    page.locator('[id="doubleClickBtn"]').dblclick()
    expect(page.locator('#doubleClickMessage')).to_have_text("You have done a double click")
    expect(page.locator('#dynamicClickMessage')).to_contain_text("You have done a dynamic click")
    page.wait_for_timeout(3000)


def test_playwright_basic_test_2(page: Page):
    full_name = "Alex Komanov"
    email = "akomanov@gmail.com"
    page.goto("https://demoqa.com/text-box")
    page.get_by_placeholder("Full Name").fill(full_name)
    page.wait_for_timeout(1000)
    page.locator("#userEmail").press_sequentially(email, delay=150)
    page.get_by_role("button", name="Submit", exact=True).click(timeout=10000)
    expect(page.locator('[id="name"]')).to_have_text(f"Name:{full_name}")
    expect(page.locator('[id="email"]')).to_have_text(f"Email:{email}")
