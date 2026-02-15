from playwright.sync_api import Page
from utils.constants import BASE_URL

class MainPage:
    def __init__(self, page: Page):
        self.__page = page
        self.__login_button = page.get_by_role("button", name="Login")

    def open_page(self):
        self.__page.goto(BASE_URL)

    def click_login_button(self):
        self.__login_button.click()