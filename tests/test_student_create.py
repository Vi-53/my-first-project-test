from logger.logger import Logger
from services.university.university_service import UniversityService
from tests.data_build import build_group_request, build_student_request


class TestStudent:
    def test_student_create(self, university_api_utils_admin):
        university_service = UniversityService(api_utils=university_api_utils_admin)

        Logger.info("### Step 1. Create group")
        group_response = university_service.create_group(
            group_request=build_group_request()
        )

        Logger.info("### Step 2. Create student")
        student_response = university_service.create_student(
            student_request=build_student_request(
                group_id=group_response.id
            )
        )

        assert student_response.group_id == group_response.id, (
            f"Wrong group id"
            f"Actual: '{student_response.group_id}'"
            f"expected: '{group_response.id}'"
        )
