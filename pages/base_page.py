from playwright.sync_api import Page

from ui.page_actions import PageActions


class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)
