from playwright.sync_api import Page

def test_playwright_basic_test_1(page: Page):
    page.goto("https://demoqa.com/buttons")
    # page.get_by_role("button", name="Click Me").nth(2).click() # nth()
    # page.get_by_role("button", name="Click Me").last.click() # last
    page.get_by_role("button", name="Click Me", exact=True).click(timeout=10000)
    page.locator('[id="doubleClickBtn"]').dblclick()
    page.wait_for_timeout(3000)
