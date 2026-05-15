from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class ScrollPage(BasePage):
    PATH = "/infinite_scroll"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.paragraphs = MultiWebElement(
            locator = self.page.locator("//*[@class='jscroll-added']"),
            description = "infinite scroll page -> loaded paragraphs",
        )

    def scroll_paragraphs_min_ten(
        self,
        expected_count: int,
        max_scroll: int = 20,
    ) -> int:

        for _ in range(max_scroll):
            current_count = self.get_paragraphs_count()

            if current_count >= expected_count:
                return current_count

            self.page.mouse.wheel(0,1000)
            self.page.wait_for_timeout(500)

        return self.get_paraghraphs_count()

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()
