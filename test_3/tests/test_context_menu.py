from pages.context_menu_page import ContextMenuPage


def test_context_click(page):
    context_menu_page = ContextMenuPage(page)

    context_menu_page.open()

    alert_message = context_menu_page.right_click_hot_spot()
    assert alert_message == ContextMenuPage.ALERT_TEXT
