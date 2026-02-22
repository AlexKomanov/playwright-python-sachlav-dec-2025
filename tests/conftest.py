from pathlib import Path

import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from playwright.sync_api import Page
from slugify import slugify


@pytest.fixture
def main_page(page: Page):
    return MainPage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach Playwright artifacts to Allure before it finalizes each phase.

    - call phase:     page is alive → take screenshot, save video path
    - teardown phase: fixtures torn down → attach video & trace from disk
    """
    if call.when == "call":
        page = item.funcargs.get("page")
        if page:
            try:
                allure.attach(
                    page.screenshot(full_page=True),
                    name="Screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception:
                pass

            try:
                if page.video:
                    item._video_path = str(page.video.path())
            except Exception:
                pass

    elif call.when == "teardown":
        video_path = getattr(item, "_video_path", None)
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name="Video",
                attachment_type="video/webm",
                extension="webm",
            )

        test_results_dir = Path("test-results")
        if test_results_dir.exists():
            expected_dir = test_results_dir / slugify(item.nodeid)
            if expected_dir.is_dir():
                trace_file = expected_dir / "trace.zip"
                if trace_file.exists():
                    allure.attach.file(
                        str(trace_file),
                        name="Trace (open at trace.playwright.dev)",
                        attachment_type="application/zip",
                        extension="zip",
                    )

    outcome = yield