from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class DynamicContentPage(BasePage):
    PATH = "/dynamic_content"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.images = MultiWebElement(
            locator = self.page.locator("//*[@id='content']//img"),
            description = "dynamic content page -> images",
        )

    def get_two_images_match(self, max_attempts: int = 15) -> bool:
        for _ in range(max_attempts):
            image_sources = self.get_image_sources()

            if self._has_dublicates(image_sources):
                return True

            self.page.reload()
            self.actions.wait_for_load_state("load")

        return False

    def get_image_sources(self) -> list[str]:
        sources = []

        for image in self.images:
            sourse = image.get_attribute("src")

            if sourse is not None:
                sources.append(sourse)

        return sources

    @staticmethod
    def _has_dublicates(values: list[str]) -> bool:
        return len(values) != len(set(values))