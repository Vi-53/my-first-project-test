from playwright.sync_api import Page

from config.settings import BASE_URL
from pages.base_page import BasePage
from ui.web_element import WebElement
from utils.url_utils import embed_credentials_in_url

class BasicAuthPage(BasePage):
    PATH = "/basic_auth"

    SUCCESS_TEXT = "Congratulations! You must have the proper credentials."

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.success_message = WebElement(
            locator = self.page.locator("//p"),
            description="Basic auth page -> Success message",
        )

    def open_with_credentials(self, username: str, password: str) -> None:
        url = embed_credentials_in_url(
            url=f"{BASE_URL}{self.PATH}",
            username=username,
            password=password,
        )

        self.actions.goto(url)

    def get_success_message(self) -> str:
        return self.success_message.get_inner_text()


