import requests

from services.general.helpers.base_helper import BaseHelper
from utils.params_utils import remove_none_values


class GradesHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}"
    STATS_ENDPOINT = f"{ENDPOINT_PREFIX}/stats"

    def get_grades(self, params: dict | None = None) -> requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT, params=params)
        return response

    def get_stats(
            self,
            student_id: int | str | None = None,
            teacher_id: int | str | None = None,
            group_id: int | str | None = None,
    ) -> requests.Response:
        params = remove_none_values(
            {
                "student_id": student_id,
                "teacher_id": teacher_id,
                "group_id": group_id,
            }
        )

        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return response
