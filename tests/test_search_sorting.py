import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchPage
from utils.enum import SortType


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize("n", [10, 15])
@pytest.mark.parametrize("filter_type",
    [SortType.LOW_TO_HIGH, SortType.HIGH_TO_LOW]
                         )

def test_1(page, config, name, n, filter_type):
    page.goto(config.base_url)

    home_page = HomePage(page)
    search_page = SearchPage(page)

    home_page.search(name)

    search_page.take_filter(filter_type)
    prices = search_page.get_n_prices(n)

    assert len(prices) >= n, f"Найдено меньше {n} цен, Всего: {len(prices)}"

    if filter_type == SortType.LOW_TO_HIGH:
        assert prices == sorted(prices), \
            f"Цены не отсортированы по возрастанию: {prices}"

    elif filter_type == SortType.HIGH_TO_LOW:
        assert prices == sorted(prices, reverse=True), \
            f"Цены не отсортированы по убыванию: {prices}"