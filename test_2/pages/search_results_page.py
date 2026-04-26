from pages.base_page import BasePage


class SearchPage(BasePage):
    FILTER = "//*[@id='sort']"
    PRICES = "//*[starts-with(@data-testid, 'search-result-price-')]"

    def take_filter(self, filter_type: str):
        self.page.locator(self.FILTER).select_option(label=filter_type)
        self.page.wait_for_load_state("networkidle")

    def get_n_prices(self, n: int):
        prices = self.page.locator(self.PRICES).all_inner_texts()
        list_price = []

        for price in prices[:n]:
            clear = price.replace("RUB", "").strip()
            list_price.append(float(clear))
        return list_price

    @staticmethod
    def low_to_high(list_price: list[float]):
        return list_price == sorted(list_price)

    @staticmethod
    def high_to_low(list_price: list[float]):
        return list_price == sorted(list_price, reverse=True)

