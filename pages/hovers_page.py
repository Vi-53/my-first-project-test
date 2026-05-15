from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement
from ui.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    PATH = "/hovers"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.users = MultiWebElement(
            locator = self.page.locator("//*[@class='figure']"),
            description = "Hovers page -> Users",
        )

    def get_users_count(self) -> int:
        return self.users.count()

    def hover_user(self, index: int) -> None:
        self.users.nth(index).hover()

    def get_user_name(self, index: int) -> str:
        user_name =WebElement(
            locator = self.page.locator("//*[@class='figure']").nth(index).locator("//h5"),
            description = f"Hovers page -> User {index + 1} name",
        )

        return user_name.get_inner_text()