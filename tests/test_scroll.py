from pages.scroll_page import ScrollPage
from config.routes import INFINITE_SCROLL_URL


def test_scroll(page, actions):
    expected_paragraphs_count = 10

    actions.goto(INFINITE_SCROLL_URL)

    scroll_page = ScrollPage(page)

    actual_paragraphs_count = (
        scroll_page.scroll_until_paragraphs_count_at_least(
            expected_count=expected_paragraphs_count,
        )
    )
    assert actual_paragraphs_count >= expected_paragraphs_count
