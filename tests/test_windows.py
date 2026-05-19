from pages.windows_page import WindowsPage
from pages.new_window_page import NewWindowPage
from config.routes import WINDOWS_URL


def test_windows(page, actions):
    expected_new_window_text = "New Window"
    expected_open_pages_count = 1

    actions.goto(WINDOWS_URL)

    windows_page = WindowsPage(page)

    with actions.expect_new_page() as first_page_info:
        windows_page.click_here()

    first_page = first_page_info.value
    first_window_page = NewWindowPage(first_page)

    assert first_window_page.get_header_text() == expected_new_window_text

    actions.bring_to_front()

    with actions.expect_new_page() as second_page_info:
        windows_page.click_here()

    second_page = second_page_info.value
    second_window_page = NewWindowPage(second_page)

    assert second_window_page.get_header_text() == expected_new_window_text

    actions.bring_to_front()

    first_page.close()
    second_page.close()

    assert len(page.context.pages) == expected_open_pages_count
