from requests import Response

from config.settings import AUTH_SERVICE_URL
from helpers.base_helper import BaseHelper


class AuthHelper(BaseHelper):
    REGISTER_PATH = "/auth/register/"
    LOGIN_PATH = "/auth/login/"

    def __init__(self) -> None:
        super().__init__(base_url=AUTH_SERVICE_URL)

    def register(
            self,
            username: str,
            password: str,
            password_repeat:str,
            email: str
    ) -> Response:
        return self.post(
            path=self.REGISTER_PATH,
            data={
                'username': username,
                'password': password,
                'password_repeat': password_repeat,
                'email': email,
            },
        )

    def login(
            self,
            username: str,
            password: str,
    ) -> Response:
        return self.post(
            path=self.LOGIN_PATH,
            data={
                'username': username,
                'password': password,
            },
        )
