from pathlib import Path

import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from playwright.sync_api import Page


@pytest.fixture
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    test_results_dir = Path("test-results")
    if not test_results_dir.exists():
        return

    # pytest-playwright stores artifacts in test-results/<test-file-name>-<test-name>-<browser>/
    # Match the current test to its artifact directory
    test_name = item.name
    test_file = Path(item.fspath).stem

    for artifact_dir in test_results_dir.iterdir():
        if not artifact_dir.is_dir():
            continue

        dir_name = artifact_dir.name
        if test_file not in dir_name or test_name not in dir_name:
            continue

        for file in artifact_dir.iterdir():
            if not file.is_file():
                continue

            if file.suffix == ".png":
                allure.attach.file(
                    str(file),
                    name=file.stem,
                    attachment_type=allure.attachment_type.PNG,
                )
            elif file.suffix == ".webm":
                allure.attach.file(
                    str(file),
                    name="Video",
                    attachment_type="video/webm",
                    extension="webm",
                )
            elif file.suffix == ".zip" and "trace" in file.stem:
                allure.attach.file(
                    str(file),
                    name="Trace (open at trace.playwright.dev)",
                    attachment_type="application/zip",
                    extension="zip",
                )