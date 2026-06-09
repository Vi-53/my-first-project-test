from typing import Any

from requests import Response

from config.settings import UNIVERSITY_SERVICE_URL
from helpers.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    GRADES_PATH = "/grades/"
    STATS_PATH = "/grades/stats/"
    GROUPS_PATH = "/groups/"
    STUDENTS_PATH = "/students/"
    TEACHERS_PATH = "/teachers/"

    def __init__(self) -> None:
        super().__init__(base_url=UNIVERSITY_SERVICE_URL)

    def get_grades(
            self,
            params: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.get(
            path=self.GRADES_PATH,
            params=params,
            headers=headers,
        )

    def get_stats(
            self,
            params: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.get(
            path=self.STATS_PATH,
            params=params,
            headers=headers
        )

    def create_group(
            self,
            name: str,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.post(
            path=self.GROUPS_PATH,
            json_body={
                "name": name,
            },
            headers=headers,
        )

    def create_teacher(
            self,
            first_name: str,
            last_name: str,
            subject: str,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.post(
            path=self.TEACHERS_PATH,
            json_body={
                "first_name": first_name,
                "last_name": last_name,
                "subject": subject,
            },
            headers=headers,
        )

    def create_student(
            self,
            first_name: str,
            last_name: str,
            email: str,
            degree:str,
            phone: str,
            group_id: int,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.post(
            path=self.STUDENTS_PATH,
            json_body={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "degree": degree,
                "phone": phone,
                "group_id": group_id,
            },
            headers=headers,
        )

    def create_grade(
            self,
            teacher_id: int,
            student_id: int,
            grade: int,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return self.post(
            path=self.GRADES_PATH,
            data={
                "teacher_id": teacher_id,
                "student_id": student_id,
                "grade": grade,
            },
            headers=headers,
        )