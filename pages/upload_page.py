from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class UploadPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.file_input = WebElement(
            locator=self.page.locator("//*[@id='file-upload']"),
            description="upload page -> upload input",
        )

        self.upload_button = WebElement(
            locator=self.page.locator("//*[@id='file-submit']"),
            description="upload page -> upload button",
        )

        self.success_message = WebElement(
            locator=self.page.locator("//*[@class='example']/h3"),
            description="upload page -> success message",
        )

        self.uploaded_file_name = WebElement(
            locator=self.page.locator("//*[@id='uploaded-files']"),
            description="upload page -> success message",
        )

    def upload_file(self, file_path: Path) -> None:
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def get_success_text(self) -> str:
        return self.success_message.get_inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.get_inner_text()
