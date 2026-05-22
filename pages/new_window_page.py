from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class NewWindowPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.header = WebElement(
            locator=self.page.locator("h3"),
            description="New window page -> Header",
        )

    def get_header_text(self) -> str:
        return self.header.get_inner_text()
