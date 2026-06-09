from typing import Any
from uuid import uuid4
from random import randint, choice

import pytest


UNKNOWN_STUDENT_ID = 99999999

def calculate_expected_stats(
        grades: list[dict[str, Any]],
) -> dict[str, int | float| None]:
    grade_value = [grade["grade"] for grade in grades]
    if not grade_value:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "avg": None,
        }
    return {
        "count": len(grade_value),
        "min": min(grade_value),
        "max": max(grade_value),
        "avg": sum(grade_value) / len(grade_value),
    }

def assert_stats_equal(
        actual: dict[str, Any],
        expected: dict[str, int | float| None],
) -> None:
    assert actual["count"] == expected["count"]
    assert actual["min"] == expected["min"]
    assert actual["max"] == expected["max"]

    if expected["avg"] is None:
        assert actual["avg"] is None
    else:
        assert actual["avg"] == pytest.approx(expected["avg"])

def get_grades_body(
        grades_helper,
        auth_headers,
        params: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    response = grades_helper.get_grades(
        params=params,
        headers=auth_headers,
    )
    assert response.status_code == 200, response.text
    return response.json()

def get_stats_body(
        grades_helper,
        auth_headers,
        params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    response = grades_helper.get_stats(
        params=params,
        headers=auth_headers,
    )
    assert response.status_code == 200, response.text
    return response.json()

def assert_status_code(
        response,
        expected_status_code: int,
        step_name: str,
) -> None:
    assert response.status_code == expected_status_code, (
        f"\n[FAILED STEP] {step_name}"
        f"\nExpected status: {expected_status_code}"
        f"\nActual status: {response.status_code}"
        f"\nResponse body: {response.text}"
        f"\nRequest URL: {response.url}"
    )

def create_grades_scenario(
        grades_helper,
        auth_headers,
) -> dict[str, Any]:
    unique_suffix = uuid4().hex[:8]

    group_response = grades_helper.create_group(
        name=f"Group_{unique_suffix}",
        headers=auth_headers,
    )

    assert_status_code(
        response=group_response,
        expected_status_code=201,
        step_name="Создание группы",
    )

    group = group_response.json()
    group_id = group["id"]

    teacher_response = grades_helper.create_teacher(
        first_name=f"Teacher{unique_suffix}",
        last_name=f"Last{unique_suffix}",
        subject="History",
        headers=auth_headers,
    )

    assert_status_code(
        response=teacher_response,
        expected_status_code=201,
        step_name="Создание преподавателя",
    )

    teacher = teacher_response.json()

    student_response = grades_helper.create_student(
        first_name=f"Student{unique_suffix}",
        last_name=f"Last{unique_suffix}",
        email=f"student_{unique_suffix}@example.com",
        degree="Bachelor",
        phone=f"+7800{randint(1000000, 9999999)}",
        group_id=group_id,
        headers=auth_headers,
    )

    assert_status_code(
        response=student_response,
        expected_status_code=201,
        step_name="Создание студента",
    )

    student = student_response.json()

    grades_count = randint(3, 6)

    grade_values = [
        randint(2,5)
        for _ in range(grades_count)
    ]
    created_grades = []

    for grade_value in grade_values:
        grade_response = grades_helper.create_grade(
            student_id=student["id"],
            teacher_id=teacher["id"],
            grade=grade_value,
            headers=auth_headers,
        )
        assert grade_response.status_code == 201, (
            f"Не удалось создать оценку {grade_value}. "
            f"Status: {grade_response.status_code}. "
            f"Body: {grade_response.text}"
        )
        created_grades.append(grade_response.json())

    return {
        "student_id": student["id"],
        "teacher_id": teacher["id"],
        "grades": created_grades,
        "group_id": group_id,
    }

def test_get_grades_stats_calculates_total_stats_correctly(
        grades_helper,
        auth_headers,
):
    grades = get_grades_body(
        grades_helper=grades_helper,
        auth_headers=auth_headers,
    )
    expected_stats = calculate_expected_stats(grades)

    actual_stats = get_stats_body(
        grades_helper=grades_helper,
        auth_headers=auth_headers,
    )
    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )

def test_get_grades_stats_for_unknown_student_returns_empty_stats(
        grades_helper,
        auth_headers,
):
    actual_stats = get_stats_body(
        grades_helper=grades_helper,
        auth_headers=auth_headers,
        params={"student_id": UNKNOWN_STUDENT_ID},
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
    ],
)
def test_get_grades_stats_calculates_filtered_stats_correctly(
        grades_helper,
        auth_headers,
        param_name,
):
    scenario = create_grades_scenario(
        grades_helper=grades_helper,
        auth_headers=auth_headers,
    )
    param_value = scenario[param_name]
    params = {param_name: param_value}

    expected_stats = calculate_expected_stats(
        scenario["grades"],
    )
    actual_stats = get_stats_body(
        grades_helper=grades_helper,
        auth_headers=auth_headers,
        params=params,
    )
    assert_stats_equal(
        actual=actual_stats,
        expected=expected_stats,
    )