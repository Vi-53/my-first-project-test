import pytest

from services.university.models.grade_response import GradeResponse
from services.university.models.grade_stats_response import GradeStatsResponse
from tests.assertions import assert_stats_equal
from tests.scenarios import create_grades_scenario, create_student_scenario


def calculate_expected_stats(
        grades: list[GradeResponse],
) -> GradeStatsResponse:
    grade_values = [grade.grade for grade in grades]

    if not grade_values:
        return GradeStatsResponse(
            count=0,
            min=None,
            max=None,
            avg=None,
        )


    return GradeStatsResponse(
        count=len(grade_values),
        min=min(grade_values),
        max=max(grade_values),
        avg=sum(grade_values) / len(grade_values),
    )

def test_get_grades_stats_calculates_total_stats_correctly(
        university_service_admin,
):
    grades = university_service_admin.get_grades()

    expected_stats = calculate_expected_stats(grades=grades)

    actual_stats = university_service_admin.get_grade_stats()

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )


def test_get_grades_stats_for_student_without_returns_empty_stats(
        university_service_admin,
):
    create_grades_scenario(
        university_service_admin=university_service_admin
    )

    student_without_grades_scenario = create_student_scenario(
        university_service_admin=university_service_admin,
    )

    student_without_grades = student_without_grades_scenario["student"]

    actual_stats = university_service_admin.get_grade_stats(
        student_id=student_without_grades.id,
    )

    expected_stats = GradeStatsResponse(
        count=0,
        min=None,
        max=None,
        avg=None,
    )

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )


@pytest.mark.parametrize(
    "param_name",
    [
        "student_id",
        "teacher_id",
        "group_id"
    ]
)
def test_get_grades_stats_calculates_filtered_stats_correctly(
        university_service_admin,
        param_name,
):
    scenario = create_grades_scenario(
        university_service_admin=university_service_admin,
    )

    param_value = scenario[param_name]

    expected_stats = calculate_expected_stats(
        grades=scenario["grades"],
    )

    actual_stats = university_service_admin.get_grade_stats(
        **{param_name: param_value},
    )

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )

def test_get_grades_stats_calculates_stats_with_student_and_teacher_filters(
        university_service_admin,
):
    scenario = create_grades_scenario(
        university_service_admin=university_service_admin,
    )

    expected_stats = calculate_expected_stats(
        grades=scenario["grades"],
    )

    actual_stats = university_service_admin.get_grade_stats(
        student_id=scenario["student_id"],
        teacher_id=scenario["teacher_id"],
    )

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )
