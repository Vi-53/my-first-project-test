import random

from faker import Faker

from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest

faker = Faker()


def build_group_request() -> GroupRequest:
    return GroupRequest(
        name=faker.company(),
    )


def build_teacher_request() -> TeacherRequest:
    return TeacherRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        subject=random.choice([option for option in SubjectEnum]),
    )


def build_student_request(group_id: int) -> StudentRequest:
    return StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.unique.email(),
        degree=random.choice([option for option in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        group_id=group_id,
    )
