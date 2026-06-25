import pytest

from tests.assertions import assert_status_code, assert_response_has_field

OPENAPI_ENDPOINT = "/openapi.json"

OPENAPI_REQUIRED_FIELDS = [
    "openapi",
    "paths",
]


def test_auth_service_openapi_status_code_200(auth_api_utils_anonym):
    response = auth_api_utils_anonym.get(OPENAPI_ENDPOINT)

    assert_status_code(
        response=response,
        expected_status_code=200,
    )


@pytest.mark.parametrize("field_name", OPENAPI_REQUIRED_FIELDS)
def test_auth_service_openapi_response_has_required_field(
        auth_api_utils_anonym,
        field_name
):
    response = auth_api_utils_anonym.get(OPENAPI_ENDPOINT)
    body = response.json()

    assert_response_has_field(
        body=body,
        field_name=field_name,
    )


def test_university_service_openapi_status_code_200(university_api_utils_anonym):
    response = university_api_utils_anonym.get(OPENAPI_ENDPOINT)

    assert_status_code(
        response=response,
        expected_status_code=200,
    )


@pytest.mark.parametrize("field_name", OPENAPI_REQUIRED_FIELDS)
def test_university_service_openapi_response_has_required_field(
        university_api_utils_anonym,
        field_name,
):
    response = university_api_utils_anonym.get(OPENAPI_ENDPOINT)
    body = response.json()

    assert_response_has_field(
        body=body,
        field_name=field_name,
    )
