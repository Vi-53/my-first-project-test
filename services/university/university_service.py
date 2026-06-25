from services.general.base_service import BaseService
from services.university.helpers.grades_helper import GradesHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.grade_request import GradeRequest
from services.university.models.grade_response import GradeResponse
from services.university.models.grade_stats_response import GradeStatsResponse
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse
from services.university.models.student_request import StudentRequest
from services.university.models.student_response import StudentResponse
from services.university.models.teacher_request import TeacherRequest
from services.university.models.teacher_response import TeacherResponse

from utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)
        self.teacher_helper = TeacherHelper(self.api_utils)
        self.grades_helper = GradesHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        response = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**response.json())

    def create_grade(self, grade_request: GradeRequest) -> GradeResponse:
        response = self.grades_helper.post_grade(data=grade_request.model_dump())
        return GradeResponse(**response.json())

    def get_grades(self, params: dict | None = None) -> list[dict]:
        response = self.grades_helper.get_grades(params=params)
        return response.json()

    def get_grade_stats(self, params: dict | None = None) -> GradeStatsResponse:
        response = self.grades_helper.get_stats(params=params)
        return GradeStatsResponse(**response.json())

    def get_students(self, params: dict | None = None) -> list[dict]:
        response = self.student_helper.get_students(params=params)
        return response.json()
