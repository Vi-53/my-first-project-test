from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_INPUT = "//*[@id='search']"
    SEARCH_BUTTON = "//*[@data-testid='search-button']"

    def open_base_url(self, base_url: str):
        self.open(base_url)

    def search(self, name: str):
        self.page.locator(self.SEARCH_INPUT).fill(name)
        self.page.locator(self.SEARCH_BUTTON).click()
