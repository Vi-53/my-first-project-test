from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.filter = page.locator("//*[@id='sort']")
        self.search_prices = page.locator("//*[starts-with(@data-testid, 'search-result-price-')]")

    def take_filter(self, filter_type: str):
        self.filter.select_option(label=filter_type)
        self.page.wait_for_load_state("networkidle")

    def get_n_prices(self, n: int):
        prices = self.search_prices.all_inner_texts()
        list_price = []

        for price in prices[:n]:
            clear = price.replace("RUB", "").strip()
            list_price.append(float(clear))
        return list_price

