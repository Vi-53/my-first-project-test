from pages.basic_auth_page import BasicAuthPage
from config.routes import BASIC_AUTH_URL
from utils.url_utils import embed_credentials_in_url


def test_basic_authorization(page, actions):
    url = embed_credentials_in_url(
        url=BASIC_AUTH_URL,
        username="admin",
        password="admin",
    )

    actions.goto(url)

    basic_auth_page = BasicAuthPage(page)

    actual_text = basic_auth_page.get_success_message()

    assert actual_text == BasicAuthPage.SUCCESS_TEXT
