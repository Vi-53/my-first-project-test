from faker import Faker

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.login_response import LoginResponse
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

    assert login_response.access_token != "", (
        f"Access token should not be empty"
        f"Actual: '{login_response.access_token}', expected not empty string"
    )
