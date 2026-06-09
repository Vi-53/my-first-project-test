from config.settings import TEST_PASSWORD, TEST_USERNAME


def test_login_returns_access_token(auth_helper):
    response = auth_helper.login(
        username=TEST_USERNAME,
        password=TEST_PASSWORD,
    )

    assert response.status_code == 200, response.text

    body = response.json()

    assert "access_token" in body
    assert "token_type" in body

    assert isinstance(body["access_token"], str)
    assert body["access_token"] != ""

    assert body["token_type"] == "Bearer"