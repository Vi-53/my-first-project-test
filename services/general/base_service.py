from typing import TypeVar

import requests
from pydantic import BaseModel

from utils.api_utils import ApiUtils

SuccessModelType = TypeVar("SuccessModelType", bound=BaseModel)
ErrorModelType = TypeVar("ErrorModelType", bound=BaseModel)


class BaseService:
    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils

    @staticmethod
    def build_response_model(
            response: requests.Response,
            success_model: type[SuccessModelType],
            error_model: type[ErrorModelType],
    ) -> SuccessModelType | ErrorModelType:
        if 200 <= response.status_code < 300:
            return success_model(**response.json())

        return error_model(**response.json())