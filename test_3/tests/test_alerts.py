from faker import Faker

from pages.alerts_page import AlertsPage


fake = Faker()


def  test_alerts(page):
    alerts_page = AlertsPage(page)

    alerts_page.open()

    alert_message = alerts_page.click_alert_and_accept()

    assert alert_message == AlertsPage.ALERT_TEXT
    assert alerts_page.get_result_text() == AlertsPage.RESULT_ALERT_TEXT

    confirm_message = alerts_page.click_confirm_and_accept()
    assert confirm_message == AlertsPage.CONFIRM_TEXT
    assert alerts_page.get_result_text() == AlertsPage.RESULT_CONFIRM_TEXT

    prompt_text = fake.word()
    prompt_message = alerts_page.click_prompt_and_accept(prompt_text)
    assert prompt_message == AlertsPage.PROMPT_TEXT
    assert alerts_page.get_result_text() == f"You entered: {prompt_text}"