import pytest

from config.settings import AUTH_SERVICE_URL, UNIVERSITY_SERVICE_URL, TEST_PASSWORD, TEST_USERNAME
from helpers.base_helper import BaseHelper
from helpers.auth_helper import AuthHelper
from helpers.grades_helper import GradesHelper


@pytest.fixture
def auth_api() -> BaseHelper:
    return BaseHelper(base_url=AUTH_SERVICE_URL)

@pytest.fixture
def university_api() -> BaseHelper:
    return BaseHelper(base_url=UNIVERSITY_SERVICE_URL)

@pytest.fixture
def auth_helper() ->AuthHelper:
    return AuthHelper()

@pytest.fixture
def grades_helper() -> GradesHelper:
    return GradesHelper()

@pytest.fixture
def auth_headers(auth_helper) -> dict[str, str]:
    response = auth_helper.login(
        username=TEST_USERNAME,
        password=TEST_PASSWORD,
    )

    assert response.status_code == 200, response.text

    body = response.json()

    return {"Authorization": f"{body['token_type']} {body['access_token']}"}