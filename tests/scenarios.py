from random import randint
from typing import Any

from services.university.models.grade_request import (
    GradeRequest,
    MAX_GRADE,
    MIN_GRADE,
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


def create_grades_scenario(university_service_admin) -> dict[str, Any]:
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

    grades_count = randint(MIN_GRADES_COUNT, MAX_GRADES_COUNT)

    create_grades = []

    for _ in range(grades_count):
        grade_value = randint(MIN_GRADE, MAX_GRADE)

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
        "grades": create_grades,
        "group_id": group_response.id,
    }
