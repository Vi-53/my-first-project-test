from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class BasicAuthPage(BasePage):
    SUCCESS_TEXT = "Congratulations! You must have the proper credentials."

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.success_message = WebElement(
            locator=self.page.locator("//p"),
            description="Basic auth page -> Success message",
        )

    def get_success_message(self) -> str:
        return self.success_message.get_inner_text()
