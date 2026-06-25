import pytest

from tests.assertions import (
    assert_json_content_type,
    assert_response_field_type,
    assert_response_field_value,
    assert_response_has_field,
    assert_status_code,
)

INVALID_ID_VALUE = "abs"

GRADES_STATS_REQUIRED_FIELDS = [
    "count",
    "min",
    "max",
    "avg",
]


def test_grades_stats_without_auth_returns_403(grades_helper_anonym):
    response = grades_helper_anonym.get_stats()

    assert_status_code(
        response=response,
        expected_status_code=403,
    )


def test_grades_stats_without_auth_response_detail_is_access_denied(grades_helper_anonym):
    response = grades_helper_anonym.get_stats()
    body = response.json()

    assert_response_field_value(
        body=body,
        field_name="detail",
        expected_value="Access denied",
    )


def test_grades_stats_success_status_code_200(grades_helper_admin):
    response = grades_helper_admin.get_stats()

    assert_status_code(
        response=response,
        expected_status_code=200,
    )


def test_grades_stats_success_content_type_json(grades_helper_admin):
    response = grades_helper_admin.get_stats()

    assert_json_content_type(
        response=response,
    )


@pytest.mark.parametrize(
    "field_name",
    GRADES_STATS_REQUIRED_FIELDS,
)
def test_grades_stats_success_response_has_required_fields(
        grades_helper_admin,
        field_name,
):
    response = grades_helper_admin.get_stats()
    body = response.json()

    assert_response_has_field(
        body=body,
        field_name=field_name,
    )


def test_grades_stats_count_is_integer(grades_helper_admin):
    response = grades_helper_admin.get_stats()
    body = response.json()

    assert_response_field_type(
        body=body,
        field_name="count",
        expected_type=int,
    )


@pytest.mark.parametrize(
    "param_name",
    [
        "student_id",
        "teacher_id",
        "group_id",
    ],
)
def test_get_grades_stats_with_invalid_id_returns_422(
        grades_helper_admin,
        param_name,
):
    response = grades_helper_admin.get_stats(
        params={param_name: INVALID_ID_VALUE},
    )

    assert_status_code(
        response=response,
        expected_status_code=422,
    )
