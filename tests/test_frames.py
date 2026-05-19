from pages.frames_page import FramesPage
from config.routes import FRAMES_URL


def test_frames(page, actions):
    actions.goto(FRAMES_URL)

    frames_page = FramesPage(page)

    assert frames_page.get_left_frame_text() == "LEFT"
    assert frames_page.get_right_frame_text() == "RIGHT"
    assert frames_page.get_bottom_frame_text() == "BOTTOM"
    assert frames_page.get_middle_frame_text() == "MIDDLE"
