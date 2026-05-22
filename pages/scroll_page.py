from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class ScrollPage(BasePage):
    PARAGRAPH_SELECTOR = ".jscroll-added"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.paragraphs = MultiWebElement(
            locator=self.page.locator(self.PARAGRAPH_SELECTOR),
            description="infinite scroll page -> loaded paragraphs",
        )

    def scroll_until_paragraphs_count_at_least(
            self,
            expected_count: int,
            timeout: int = 30_000,
    ) -> int:
        self._wait_until_paragraphs_count_at_least(
            expected_count=expected_count,
            timeout=timeout,
        )

        return self.get_paragraphs_count()

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

    def _wait_until_paragraphs_count_at_least(
            self,
            expected_count: int,
            timeout: int,
    ) -> None:
        try:
            self.page.wait_for_function(
                """
                ([selector, expectedCount]) => {
                    window.scrollTo(0, document.documentElement.scrollHeight);

                    return document.querySelectorAll(selector).length >= expectedCount;
                }
                """,
                arg=[self.PARAGRAPH_SELECTOR, expected_count],
                timeout=timeout,
                polling=200,
            )

        except PlaywrightTimeoutError:
            return
