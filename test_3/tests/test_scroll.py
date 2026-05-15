from pages.scroll_page import ScrollPage


def test_scroll(page):
    scroll_page = ScrollPage(page)

    scroll_page.open()

    paragraphs_count = scroll_page.scroll_paragraphs_min_ten(
        expected_count=10,
    )

    assert paragraphs_count >= 10