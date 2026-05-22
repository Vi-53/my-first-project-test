from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class HoversPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.users = MultiWebElement(
            locator=self.page.locator("//*[contains(@class, 'figure')]"),
            description="Hovers page -> Users",
        )

        self.user_name = MultiWebElement(
            locator=self.page.locator("//*[contains(@class, 'figure')]").locator("//h5"),
            description=f"Hovers page -> User names",
        )

    def get_users_count(self) -> int:
        return self.users.count()

    def hover_user(self, index: int) -> None:
        self.users.nth(index).hover()

    def get_user_name(self, index: int) -> str:
        return self.user_name.nth(index).get_inner_text()
