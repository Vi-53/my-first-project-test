import time

import requests
from faker import Faker
import pytest

from services.auth.auth_service import AuthService
from services.auth.models.login_request import LoginRequest
from services.auth.models.register_request import RegisterRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils
from services.university.helpers.grades_helper import GradesHelper

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()))
    login_response = auth_service.login_user(
        login_request=LoginRequest(
            username=username,
            password=password))

    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    return ApiUtils(
        url=AuthService.SERVICE_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=UniversityService.SERVICE_URL,
        headers={"Authorization": f"Bearer {access_token}"}
    )
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def grades_helper_anonym(university_api_utils_anonym):
    return GradesHelper(api_utils=university_api_utils_anonym)


@pytest.fixture(scope="function", autouse=False)
def grades_helper_admin(university_api_utils_admin):
    return GradesHelper(api_utils=university_api_utils_admin)


@pytest.fixture(scope="function", autouse=False)
def university_service_admin(university_api_utils_admin):
    return UniversityService(api_utils=university_api_utils_admin)


@pytest.fixture(scope="function", autouse=True)
def auth_service_readiness():
    timeout = 180
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(f"Auth service wasn't started during '{timeout}' seconds.")
