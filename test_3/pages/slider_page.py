import random

from playwright.sync_api import Page
from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderPage(BasePage):
    PATH = "/horizontal_slider"

    STEP = 0.5
    ALL_VALUES = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.slider = WebElement(
            locator = self.page.locator("//*[@type='range']"),
            description = "Slider page -> horizontal slider",
        )

        self.slider_value = WebElement(
            locator = self.page.locator("//*[@id='range']"),
            description = "Slider page -> Slider value",
        )

    def set_random_value_on_keyboard(self) -> str:
        random_value = random.choice(self.ALL_VALUES)

        self.slider.focus()

        for _ in range(10):
            # сбрасываем слайдер до нуля
            self.slider.press("ArrowLeft")

        steps_count = int(random_value / self.STEP)

        for _ in range(steps_count):
            self.slider.press("ArrowRight")

        return self._format_slider_value(random_value)

    def get_slider_value(self) -> str:
        return self.slider_value.get_inner_text()

    @staticmethod
    def _format_slider_value(value: float) -> str:
        if isinstance(value, int):
            return str(int(value))

        return str(value)
