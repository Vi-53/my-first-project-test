from faker import Faker

from config.routes import ALERTS_URL
from pages.alerts_page import AlertsPage

fake = Faker()


def test_alerts(page, actions):
    expected_alert_text = "I am a JS Alert"
    expected_confirm_text = "I am a JS Confirm"
    expected_prompt_text = "I am a JS prompt"

    expected_alert_result_text = "You successfully clicked an alert"
    expected_confirm_result_text = "You clicked: Ok"

    actions.goto(ALERTS_URL)

    alerts_page = AlertsPage(page)

    alert_message = alerts_page.click_alert_and_accept()
    actual_alert_result_text = alerts_page.get_result_text()

    assert alert_message == expected_alert_text, (
        f"Incorrect JS Alert message. "
        f"Expected: '{expected_alert_text}', actual: '{alert_message}'"
    )

    assert actual_alert_result_text == expected_alert_result_text, (
        f"Incorrect result text after JS Alert. "
        f"Expected: '{expected_alert_result_text}', actual: '{actual_alert_result_text}'"
    )

    confirm_message = alerts_page.click_confirm_and_accept()
    actual_confirm_result_text = alerts_page.get_result_text()

    assert confirm_message == expected_confirm_text, (
        f"Incorrect JS Confirm message. "
        f"Expected: '{expected_confirm_text}', actual: '{confirm_message}'"
    )

    assert actual_confirm_result_text == expected_confirm_result_text, (
        f"Incorrect result text after JS Confirm. "
        f"Expected: '{expected_confirm_result_text}', actual: '{actual_confirm_result_text}'"
    )

    prompt_text = fake.word()

    prompt_message = alerts_page.click_prompt_and_accept(prompt_text)
    actual_prompt_result_text = alerts_page.get_result_text()
    expected_prompt_result_text = f"You entered: {prompt_text}"

    assert prompt_message == expected_prompt_text, (
        f"Incorrect JS Prompt message. "
        f"Expected: '{expected_prompt_text}', actual: '{prompt_message}'"
    )

    assert actual_prompt_result_text == expected_prompt_result_text, (
        f"Incorrect result text after JS Prompt. "
        f"Expected: '{expected_prompt_result_text}', actual: '{actual_prompt_result_text}'"
    )
