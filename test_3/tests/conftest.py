import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()

@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False,
        )
        yield browser

        browser.close()

@pytest.fixture()
def page(browser: Browser) -> Page:
    context = browser.new_context(
        viewport={"width": 1440, "height": 900},
        ignore_https_errors=True,
        accept_downloads=True,
    )

    page = context.new_page()
    page.set_default_timeout(10_000)
    page.set_default_navigation_timeout(15_000)

    yield page

    context.close()