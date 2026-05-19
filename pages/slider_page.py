from playwright.sync_api import Page
from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.slider = WebElement(
            locator=self.page.locator("//*[@type='range']"),
            description="Slider page -> horizontal slider",
        )

        self.slider_value = WebElement(
            locator=self.page.locator("//*[@id='range']"),
            description="Slider page -> Slider value",
        )

    def set_value_by_keyboard(self, target_value: float) -> None:
        min_value = self.get_min_value()
        step = self.get_step()

        self.slider.focus()
        self.slider.press("Home")

        steps_count = round((target_value - min_value) / step)

        for _ in range(steps_count):
            self.slider.press("ArrowRight")

    def get_slider_value(self) -> str:
        return self.slider_value.get_inner_text()

    def get_available_non_boundary_values(self) -> list[float]:
        min_value = self.get_min_value()
        max_value = self.get_max_value()
        step = self.get_step()

        values = []
        current_value = min_value + step

        while current_value < max_value:
            values.append(round(current_value, 10))
            current_value += step

        return values

    def get_min_value(self) -> float:
        return self._get_slider_attribute_as_float("min")

    def get_max_value(self) -> float:
        return self._get_slider_attribute_as_float("max")

    def get_step(self) -> float:
        return self._get_slider_attribute_as_float("step")

    def _get_slider_attribute_as_float(self, attribute: str) -> float:
        value = self.slider.get_attribute(attribute)

        if value is None:
            raise RuntimeError(f"Slider attribute '{attribute}' was not found")

        return float(value)
