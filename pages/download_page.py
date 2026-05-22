from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class DownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.files = MultiWebElement(
            locator=self.page.locator("//*[contains(@class, 'example')]/a"),
            description="Download page -> Files",
        )

    def get_file_name_by_index(self, index: int) -> str:
        return self.files.nth(index).get_inner_text().strip()

    def download_file_by_index(self, index: int) -> str:
        file_link = self.files.nth(index)

        download = self.actions.run_and_expect_download(
            action=file_link.click,
        )

        return download.suggested_filename

    def get_files_count(self) -> int:
        return self.files.count()
