from playwright.sync_api import Frame, Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class FramesPage(BasePage):
    PATH = "/nested_frames"

    LEFT_TEXT = "LEFT"
    RIGHT_TEXT = "RIGHT"
    BOTTOM_TEXT = "BOTTOM"
    MIDDLE_TEXT = "MIDDLE"

    LEFT_FRAME = "frame-left"
    RIGHT_FRAME = "frame-right"
    BOTTOM_FRAME = "frame-bottom"
    MIDDLE_FRAME = "frame-middle"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_left_frame_text(self) -> str:
        return self._get_frame_text(self.LEFT_FRAME)

    def get_right_frame_text(self) -> str:
        return self._get_frame_text(self.RIGHT_FRAME)

    def get_bottom_frame_text(self) -> str:
        return self._get_frame_text(self.BOTTOM_FRAME)

    def get_middle_frame_text(self) -> str:
        return self._get_frame_text(self.MIDDLE_FRAME)

    def _get_frame_text(self, frame_name: str) -> str:
        frame = self._get_frame(frame_name)

        body = WebElement(
            locator=frame.locator("body"),
            description=f"Frames page -> {frame_name} body",
        )

        return body.get_inner_text().strip()

    def _get_frame(self, frame_name: str) -> Frame:
        frame = self.page.frame(name=frame_name)

        if frame is None:
            raise RuntimeError(f"Frame '{frame_name}' was not found")

        return frame