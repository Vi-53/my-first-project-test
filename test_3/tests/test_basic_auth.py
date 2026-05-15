from pages.basic_auth_page import BasicAuthPage


def test_basic_authorization(page):
    basic_auth_page = BasicAuthPage(page)

    basic_auth_page.open_with_credentials(
        username="admin",
        password="admin",
    )

    actual_text = basic_auth_page.get_success_message()

    assert actual_text == basic_auth_page.SUCCESS_TEXT