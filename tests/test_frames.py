from pages.frames_page import FramesPage


def test_frames(page):
    frames_page = FramesPage(page)

    frames_page.open()

    assert frames_page.get_left_frame_text() == FramesPage.LEFT_TEXT
    assert frames_page.get_right_frame_text() == FramesPage.RIGHT_TEXT
    assert frames_page.get_bottom_frame_text() == FramesPage.BOTTOM_TEXT
    assert frames_page.get_middle_frame_text() == FramesPage.MIDDLE_TEXT