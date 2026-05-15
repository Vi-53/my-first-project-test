from pages.slider_page import SliderPage


def test_slider(page):
    slider_page = SliderPage(page)

    slider_page.open()

    expected_value = slider_page.set_random_value_on_keyboard()
    actual_value = slider_page.get_slider_value()

    assert actual_value == expected_value