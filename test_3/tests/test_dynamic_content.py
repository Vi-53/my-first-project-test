from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(page):
    dynamic_content_page = DynamicContentPage(page)

    dynamic_content_page.open()

    has_matching_images = dynamic_content_page.get_two_images_match()

    assert has_matching_images