from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class AlertsPage(BasePage):
    PATH = "/javascript_alerts"

    ALERT_TEXT = "I am a JS Alert"
    CONFIRM_TEXT = "I am a JS Confirm"
    PROMPT_TEXT = "I am a JS prompt"

    RESULT_ALERT_TEXT = "You successfully clicked an alert"
    RESULT_CONFIRM_TEXT = "You clicked: Ok"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.js_alert_button = WebElement(
            locator=self.page.get_by_text("Click for JS Alert"),
            description="alerts page -> Click for JS Alert button"
        )

        self.js_confirm_button = WebElement(
            locator=self.page.get_by_text("Click for JS Confirm"),
            description="alerts page -> Click for JS Confirm button"
        )

        self.js_prompt_button = WebElement(
            locator=self.page.get_by_text("Click for JS Prompt"),
            description="alerts page -> Click for JS Prompt button",
        )

        self.result = WebElement(
            locator=self.page.locator("//*[@id='result']"),
            description="alerts page -> Result text",
        )

    def click_alert_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(
            action=self.js_alert_button.click,
        )

    def click_confirm_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(
            action=self.js_confirm_button.click,
        )

    def click_prompt_and_accept(self, prompt_text: str) -> str:
        return self.actions.run_and_accept_prompt(
            action=self.js_prompt_button.click,
            prompt_text=prompt_text,
        )

    def get_result_text(self) -> str:
        return self.result.get_inner_text()


