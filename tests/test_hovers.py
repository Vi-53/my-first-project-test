from pages.hovers_page import HoversPage
from config.routes import HOVERS_URL


def test_hovers(page, actions):
    actions.goto(HOVERS_URL)

    hovers_page = HoversPage(page)

    users_count = hovers_page.get_users_count()

    for index in range(users_count):
        hovers_page.hover_user(index)

        actual_name = hovers_page.get_user_name(index)
        expected_name = f"name: user{index + 1}"

        assert actual_name == expected_name
