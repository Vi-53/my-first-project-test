from typing import Any

import pytest

from tests.assertions import assert_stats_equal
from tests.scenarios import create_grades_scenario


def calculate_expected_stats(
        grades: list[dict[str, Any]],
) -> dict[str, int | float | None]:
    grade_values = [grade["grade"] for grade in grades]

    if not grade_values:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "avg": None,
        }

    return {
        "count": len(grade_values),
        "min": min(grade_values),
        "max": max(grade_values),
        "avg": sum(grade_values) / len(grade_values),
    }


def get_unknown_student_id(university_service_admin) -> int:
    students = university_service_admin.get_students()

    if not students:
        return 1
    max_student_id = max(student["id"] for student in students)

    return max_student_id + 1


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


def test_get_grades_stats_for_unknown_student_empty_stats(
        university_service_admin,
):
    unknown_student_id = get_unknown_student_id(
        university_service_admin=university_service_admin,
    )

    actual_stats = university_service_admin.get_grade_stats(
        params={"student_id": unknown_student_id},
    )

    expected_stats = {
        "count": 0,
        "min": None,
        "max": None,
        "avg": None,
    }

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )


@pytest.mark.parametrize(
    "param_name",
    [
        "student_id",
        "teacher_id",
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
        params={param_name: param_value},
    )

    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )
