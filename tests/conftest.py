import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from logger import setup_logger
from ui.page_actions import PageActions

from config.settings import (
    ACCEPT_DOWNLOADS,
    DEFAULT_TIMEOUT_MS,
    IGNORE_HTTPS_ERRORS,
    DEFAULT_NAVIGATION_TIMEOUT_MS,
    VIEWPORT,
)


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
        viewport=VIEWPORT,
        ignore_https_errors=IGNORE_HTTPS_ERRORS,
        accept_downloads=ACCEPT_DOWNLOADS,
    )

    page = context.new_page()
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    page.set_default_navigation_timeout(DEFAULT_NAVIGATION_TIMEOUT_MS)

    yield page

    context.close()


@pytest.fixture()
def actions(page: Page) -> PageActions:
    return PageActions(page)
