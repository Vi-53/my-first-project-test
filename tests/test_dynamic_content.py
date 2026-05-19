from pages.dynamic_content_page import DynamicContentPage
from config.routes import DYNAMIC_CONTENT_URL


def test_dynamic_content(page, actions):
    actions.goto(DYNAMIC_CONTENT_URL)

    dynamic_content_page = DynamicContentPage(page)

    has_matching_images = dynamic_content_page.get_two_images_match()

    assert has_matching_images
