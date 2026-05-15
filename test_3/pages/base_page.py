from playwright.sync_api import Page

from config.settings import BASE_URL
from ui.page_actions import PageActions


class BasePage:
    PATH = ""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)

    def open(self) -> None:
        self.actions.goto(f"{BASE_URL}{self.PATH}")