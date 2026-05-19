import logging
from pathlib import Path

from playwright.sync_api import Locator

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class WebElement:
    def __init__(
            self,
            locator: Locator,
            description: str) -> None:
        self.locator = locator
        self.description = description

    def __str__(self) -> str:
        return f"WebElement[{self.description}]"

    def click(self) -> None:
        """метод кликает по элементу"""
        logger.info(f"{self}: click")
        self.locator.click()

    def right_click(self) -> None:
        """метод кликает пкм"""
        logger.info(f"{self}: right_click")
        self.locator.click(button="right")

    def fill(self, value:str) -> None:
        """ метод заполняет поле ввода"""
        logger.info(f"{self}: fill with value '{value}'")
        self.locator.fill(value)

    def press(self, key: str) -> None:
        """нажимает клавишу на элементе"""
        logger.info(f"{self}: press '{key}'")
        self.locator.press(key)

    def focus(self) -> None:
        """ставить фокус на элементе(напр. на поле ввода)"""
        logger.info(f"{self}: focus")
        self.locator.focus()

    def hover(self) -> None:
        """наводит мышь на элем."""
        logger.info(f"{self}: hover")
        self.locator.hover()

    def get_inner_text(self) -> str:
        """получает видимый текст элем."""
        logger.info(f"{self}: get inner text")
        text = self.locator.inner_text()
        logger.info(f"{self}: inner text = '{text}'")
        return text

    def get_text_content(self) -> str|None:
        """получает текст из HTML, в ТЧ скрытый текст"""
        logger.info(f"{self}: get text content")
        text = self.locator.text_content()
        logger.info(f"{self}: text content = '{text}'")
        return text

    def get_attribute(self, attribute: str) -> str|None:
        """получает атрибут элем."""
        logger.info(f"{self}: get attribute '{attribute}'")
        value = self.locator.get_attribute(attribute)
        logger.info(f"{self}: attribute = '{value}'")
        return value

    def scroll_into_view_if_needed(self) -> None:
        """прокручивает страницу к элем., если он сейчас не видим"""
        logger.info(f"{self}: scroll_info_view_if_needed")
        self.locator.scroll_into_view_if_needed()

    def set_input_files(self, file_path: Path) -> None:
        """метод для загрузки файлов на сайт"""
        logger.info(f"{self}: set_input_files '{file_path}'")
        self.locator.set_input_files(file_path)