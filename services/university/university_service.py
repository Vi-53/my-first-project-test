from services.general.base_service import BaseService
from services.general.models.error_response import ErrorResponse
from services.university.helpers.grades_helper import GradesHelper
from services.university.helpers.group_helper import GroupHelper
from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_student import DegreeEnum
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
from utils.params_utils import remove_none_values


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

    def get_grades(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
    ) -> list[GradeResponse]:
        params = remove_none_values(
            {
                "student_id": student_id,
                "teacher_id": teacher_id,
            }
        )

        response = self.grades_helper.get_grades(params=params)

        return [
            GradeResponse(**grade)
            for grade in response.json()
        ]

    def get_grade_stats(
            self,
            student_id: int | None = None,
            teacher_id: int | None = None,
            group_id: int | None = None,
    ) -> GradeStatsResponse | ErrorResponse:
        response = self.grades_helper.get_stats(
            student_id=student_id,
            teacher_id=teacher_id,
            group_id=group_id,
        )
        return self.build_response_model(
            response=response,
            success_model=GradeStatsResponse,
            error_model=ErrorResponse,
        )

    def get_students(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            email: str | None = None,
            degree: DegreeEnum | None = None,
            phone: str | None = None,
            group_id: int | None = None,
    )-> list[StudentResponse]:
        params = remove_none_values(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "degree": degree.value if degree is not None else None,
                "phone": phone,
                "group_id": group_id,
            }
        )
        response = self.student_helper.get_students(params=params)
        return [
            StudentResponse(**student)
            for student in response.json()
        ]