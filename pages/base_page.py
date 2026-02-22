import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.__page = page

    @allure.step("Navigate to {url}")
    def goto(self, url: str) -> None:
        self.__page.goto(url)

    def get_page(self) -> Page:
        return self.__page

    @property
    def page(self) -> Page:
        return self.__page