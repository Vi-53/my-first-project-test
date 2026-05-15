from pages.windows_page import WindowsPage

def test_windows(page):
    windows_page = WindowsPage(page)

    windows_page.open()

    first_window = windows_page.open_new_window()

    assert windows_page.get_new_window_text(first_window) == WindowsPage.NEW_WINDOW_TEXT

    windows_page.bring_main_page_front()

    second_window = windows_page.open_new_window()

    assert windows_page.get_new_window_text(second_window) == WindowsPage.NEW_WINDOW_TEXT

    windows_page.bring_main_page_front()

    windows_page.close_window(first_window)
    windows_page.close_window(second_window)

    assert windows_page.get_open_pages_count() == 1