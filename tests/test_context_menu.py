from pages.context_menu_page import ContextMenuPage
from config.routes import CONTEXT_MENU_URL


def test_context_click(page, actions):
    actions.goto(CONTEXT_MENU_URL)

    context_menu_page = ContextMenuPage(page)

    alert_message = context_menu_page.right_click_hot_spot()
    assert alert_message == ContextMenuPage.ALERT_TEXT
