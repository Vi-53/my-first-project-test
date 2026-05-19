from playwright.sync_api import Frame, Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class FramesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        top_frame = self.page.frame_locator("frame[name='frame-top']")

        self.left_frame_body = WebElement(
            locator=top_frame.frame_locator("frame[name='frame-left']").locator("body"),
            description="Frames page -> Left frame body",
        )

        self.middle_frame_body = WebElement(
            locator=top_frame.frame_locator("frame[name='frame-middle']").locator("body"),
            description="Frames page -> Middle frame body",
        )

        self.right_frame_body = WebElement(
            locator=top_frame.frame_locator("frame[name='frame-right']").locator("body"),
            description="Frames page -> Right frame body",
        )

        self.bottom_frame_body = WebElement(
            locator=self.page.frame_locator("frame[name='frame-bottom']").locator("body"),
            description="Frames page -> Bottom frame body",
        )

    def get_left_frame_text(self) -> str:
        return self.left_frame_body.get_inner_text().strip()

    def get_right_frame_text(self) -> str:
        return self.right_frame_body.get_inner_text().strip()

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame_body.get_inner_text().strip()

    def get_middle_frame_text(self) -> str:
        return self.middle_frame_body.get_inner_text().strip()
