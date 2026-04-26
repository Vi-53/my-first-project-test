import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    return ConfigReader()

@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=config.headless)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser, config):
    context = browser.new_context()
    new_page = context.new_page()
    new_page.set_default_timeout(config.timeout)
    yield new_page
    context.close()

