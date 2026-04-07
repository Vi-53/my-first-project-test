from playwright.sync_api import Page, expect
import random
import string

def random_string(length=10):
    # тут создаю рандомные пароль и логин
    line = string.ascii_letters + string.digits
    return ''.join(random.choice(line) for _ in range(length))

def test_request(page: Page):
    # тут вхожу по ссылке на сайт и жду полного ответа
    page.goto('http://144.31.139.115:5000/.', wait_until='load')

    # тут нахожусь на главной странице, кликаю на кнопку входа и жду загрузки нового адреса
    page.get_by_test_id('nav-login').click()
    #page.get_by_role('link', name='Login').click() - или надо так??
    page.wait_for_url('**/login')

    # тут переопределяю рандомные значения
    username = random_string()
    password = random_string()

    # тут их ввожу и кликаю на вход
    page.locator('xpath=//input[@id="username"]').fill(username)
    page.locator('xpath=//input[@id="password"]').fill(password)
    page.get_by_test_id('login-submit').click()

    # тут проверяю кружок загрузки
    circle = page.get_by_test_id('login-submit-spinner')
    expect(circle).to_be_visible()
    expect(circle).to_be_hidden()

    # тут проверяю надпись об ошибке
    error_text = page.get_by_test_id('login-error-inline')
    expect(error_text).to_be_visible()
    expect(error_text).to_have_text('Invalid login or password.')












