import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchPage


@pytest.mark.parametrize(
    "name, n, filter_type",
    [
        ("city", 10, "Price: low to high"),
        ("city", 15, "Price: high to low"),
        ("habits", 10, "Price: low to high"),
        ("habits", 15, "Price: high to low"),
    ]
)

def test_1(page, config, name, n, filter_type):
    home_page = HomePage(page)
    search_page = SearchPage(page)

    home_page.open_base_url(config.base_url)
    home_page.search(name)

    search_page.take_filter(filter_type)
    prices = search_page.get_n_prices(n)

    assert len(prices) >= n, f"Найдено меньше {n} цен, Всего: {len(prices)}"

    if filter_type == "Price: low to high":
        assert search_page.low_to_high(prices), \
            f"Цены не отсортированы по возрастанию: {prices}"

    elif filter_type == "Price: high to low":
        assert search_page.high_to_low(prices), \
            f"Цены не отсортированы по убыванию: {prices}"