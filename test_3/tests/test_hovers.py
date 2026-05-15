from pages.hovers_page import HoversPage


def test_hovers(page):
    hovers_page = HoversPage(page)

    hovers_page.open()

    users_count = hovers_page.get_users_count()

    for index in range(users_count):
        hovers_page.hover_user(index)

        actual_name = hovers_page.get_user_name(index)
        expected_name = f"name: user{index+1}"

        assert actual_name == expected_name