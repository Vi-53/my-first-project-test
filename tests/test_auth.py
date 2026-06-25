from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest

faker = Faker()


def test_login_returns_access_token(auth_api_utils_anonym):
    auth_service = AuthService(api_utils=auth_api_utils_anonym)

    username = faker.unique.user_name()
    password = faker.password(
        length=30,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )

    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.unique.email(),
        )
    )

    login_response = auth_service.login_user(
        login_request=LoginRequest(
            username=username,
            password=password,
        )
    )

    assert isinstance(login_response.access_token, str), (
        f"Wrong access_token type"
        f"Actual: '{type(login_response.access_token)}', expected: 'str'"
        f"Actual value: '{login_response.access_token}'"
    )

    assert login_response.access_token != "", (
        f"Wrong access_token value"
        f"Actual: empty string, expected: non-empty access token"
    )

    assert login_response.token_type == "Bearer", (
        f"Wrong token_type"
        f"Actual: '{login_response.token_type}', expected: 'Bearer'"
    )
