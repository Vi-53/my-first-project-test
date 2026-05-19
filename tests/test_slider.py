import random

from pages.slider_page import SliderPage
from config.routes import SLIDER_URL


def test_slider(page, actions):
    actions.goto(SLIDER_URL)

    slider_page = SliderPage(page)

    available_values = slider_page.get_available_non_boundary_values()

    assert available_values, "Slider has no available non-boundary values"

    target_value = random.choice(available_values)

    slider_page.set_value_by_keyboard(target_value)

    expected_value = f"{target_value:g}"
    actual_value = slider_page.get_slider_value()

    assert actual_value == expected_value
