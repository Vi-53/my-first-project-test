from playwright.sync_api import Locator
from typing_extensions import Self

from ui.web_element import WebElement


class MultiWebElement:
    def __init__(
            self,
            locator: Locator,
            description: str,
) -> None:
        self.locator = locator
        self.description = description
        self.index = 0

    def __iter__(self) -> Self:
        # делает объект перебираемым
        self.index = 0
        return self

    def __next__(self) -> WebElement:
        # говорит, какой элем взять следующим при переборе
        if self.index >= self.count():
            raise StopIteration

        element = self.nth(self.index)
        self.index+=1

        return element

    def nth(self, index: int) -> WebElement:
        # возвращает элем по номеру
        return WebElement(
            locator=self.locator.nth(index),
            description=f"{self.description}[{index}]",
        )

    def first(self) -> WebElement:
        # возвращает первый элем из набора
        return WebElement(
            locator=self.locator.first,
            description=f"{self.description}[first]",
        )

    def last(self) -> WebElement:
        # возвращ. последний элемент из набора
        return WebElement(
            locator=self.locator.last,
            description=f"{self.description}[last]",
        )

    def count(self) -> int:
        # считает, сколько элем. найдено на странице
        return self.locator.count()

    def all(self) -> list[WebElement]:
        # возвращает список всех элементов
        return [self.nth(index) for index in range(self.count())]

    def __str__(self) -> str:
        # строковое представление объекта
        return f"MultiWebElement[{self.description}]"