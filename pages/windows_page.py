from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class WindowsPage(BasePage):
    PATH = "/windows"

    NEW_WINDOW_TEXT = "New Window"

    def __init__(self, page :Page) -> None:
        super().__init__(page)

        self.click_here = WebElement(
            locator = self.page.get_by_text('Click Here'),
            description = "Windows page -> Click here",
        )

    def open_new_window(self) -> Page:
        with self.actions.expect_new_page() as new_page_info:
            self.click_here.click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def bring_main_page_front(self) -> None:
        self.actions.bring_to_front()

    def get_open_pages_count(self) -> int:
        return len(self.page.context.pages)

    @staticmethod
    def get_new_window_text(new_page:Page) -> str:
        text_element = WebElement(
            locator = new_page.locator("//h3"),
            description = "New Window page -> text",
        )
        return text_element.get_inner_text()

    @staticmethod
    def close_window(window_page: Page) -> None:
        window_page.close()