from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class WindowsPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.click_here_link = WebElement(
            locator=self.page.get_by_text('Click Here'),
            description="Windows page -> Click here",
        )

    def click_here(self) -> None:
        self.click_here_link.click()
