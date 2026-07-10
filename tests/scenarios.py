from random import randint
from typing import Any

from services.university.models.grade_request import (
    MAX_GRADE,
    MIN_GRADE,
    GradeRequest,
)
from tests.data_build import (
    build_group_request,
    build_student_request,
    build_teacher_request,
)

MIN_GRADES_COUNT = 3
MAX_GRADES_COUNT = 6


def create_student_scenario(university_service_admin) -> dict[str, Any]:
    group_response = university_service_admin.create_group(
        group_request=build_group_request(),
    )
    student_response = university_service_admin.create_student(
        student_request=build_student_request(
            group_id=group_response.id,
        ),
    )

    return {
        "group": group_response,
        "student": student_response,
    }


def create_grades_scenario(
        university_service_admin,
        grade_values: list[int] | None = None,
) -> dict[str, Any]:
    group_response = university_service_admin.create_group(
        group_request=build_group_request(),
    )

    teacher_response = university_service_admin.create_teacher(
        teacher_request=build_teacher_request(),
    )

    student_response = university_service_admin.create_student(
        student_request=build_student_request(
            group_id=group_response.id,
        ),
    )

    if grade_values is None:
        grades_count = randint(MIN_GRADES_COUNT, MAX_GRADES_COUNT)

        grade_values = [
            randint(MIN_GRADE, MAX_GRADE) for _ in range(grades_count)
        ]

    create_grades = []

    for grade_value in grade_values:
        grade_response = university_service_admin.create_grade(
            grade_request=GradeRequest(
                student_id=student_response.id,
                teacher_id=teacher_response.id,
                grade=grade_value,
            ),
        )

        create_grades.append(grade_response)

    return {
        "student_id": student_response.id,
        "teacher_id": teacher_response.id,
        "group_id": group_response.id,
        "grades": create_grades,
    }
