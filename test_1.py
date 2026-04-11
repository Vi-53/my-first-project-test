from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()

ADRESS = 'http://144.31.139.115:5000/.'

def random_string(length=10):
    # тут создаю рандомные пароль и логин
    return fake.password(length=length)

def test_request(page: Page):
    # тут вхожу по ссылке на сайт и жду полного ответа
    page.goto(ADRESS)

    # тут нахожусь на главной странице, кликаю на кнопку входа и жду загрузки нового адреса
    page.get_by_test_id('nav-login').click()
    #page.get_by_role('link', name='Login').click() - или надо так??
    page.wait_for_url('**/login')

    # тут переопределяю рандомные значения
    username = random_string()
    password = random_string()

    # тут их ввожу и кликаю на вход
    page.locator('//*[@id="username"]').fill(username)
    page.locator('//*[@id="password"]').fill(password)
    page.get_by_test_id('login-submit').click()

    # тут проверяю кружок загрузки
    circle = page.get_by_test_id('login-submit-spinner')
    expect(circle).to_be_visible()
    expect(circle).to_be_hidden()

    # тут проверяю надпись об ошибке
    error_text = page.get_by_test_id('login-error-inline')
    assert error_text.is_visible(), "Элемент не появился:("
    assert error_text.inner_text() == 'Invalid login or password.'