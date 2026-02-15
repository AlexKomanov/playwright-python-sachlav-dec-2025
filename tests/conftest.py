import pytest
from pages.main_page import MainPage
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def main_page(page: Page):
    return MainPage(page)

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)