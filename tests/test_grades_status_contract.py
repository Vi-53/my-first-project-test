import pytest

from services.general.models.error_response import ErrorResponse
from services.university.models.grade_stats_response import GradeStatsResponse
from tests.assertions import assert_status_code

INVALID_ID_VALUE = "abs"


def test_grades_stats_without_auth_returns_403(grades_helper_anonym):
    response = grades_helper_anonym.get_stats()

    assert_status_code(
        response=response,
        expected_status_code=403,
    )


def test_grades_stats_without_auth_response_detail_is_access_denied(grades_helper_anonym):
    response = grades_helper_anonym.get_stats()

    error_response = ErrorResponse(**response.json())

    assert error_response.detail == "Access denied", (
        f"Wrong error detail"
        f"Actual: {error_response.detail}, expected: 'Access denied'"
    )


def test_grades_stats_success_status_code_200(grades_helper_admin):
    response = grades_helper_admin.get_stats()

    assert_status_code(
        response=response,
        expected_status_code=200,
    )


def test_grades_stats_success_matches_model(grades_helper_admin):
    response = grades_helper_admin.get_stats()

    GradeStatsResponse(**response.json())


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
        **{param_name: INVALID_ID_VALUE},
    )

    assert_status_code(
        response=response,
        expected_status_code=422,
    )
