from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class ContextMenuPage(BasePage):
    ALERT_TEXT = "You selected a context menu"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.hot_spot = WebElement(
            locator=self.page.locator("//*[@id='hot-spot']"),
            description="Context menu -> hot spot area",
        )

    def right_click_hot_spot(self) -> str:
        return self.actions.run_and_accept_alert(
            action=self.hot_spot.right_click,
        )
