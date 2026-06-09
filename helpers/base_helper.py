from typing import Any

import requests
from requests import Response


class BaseHelper:
    def __init__(self, base_url:str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _build_url(self, path:str) -> str:
        return f'{self.base_url}/{path.lstrip("/")}'

    def get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        return requests.get(
            url=self._build_url(path),
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def post(
            self,
            path: str,
            json_body: dict[str, Any] | None = None,
            data: dict[str, Any] | None = None,
            params: dict[str, Any] | None = None,
            headers: dict[str, str] | None = None,
    ) -> Response:
        return requests.post(
            url=self._build_url(path),
            json=json_body,
            data=data,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def put(
        self,
        path: str,
        json_body: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        return requests.put(
            url=self._build_url(path),
            json=json_body,
            data=data,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def patch(
        self,
        path: str,
        json_body: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> Response:
        return requests.patch(
            url=self._build_url(path),
            json=json_body,
            data=data,
            params=params,
            headers=headers,
            timeout=self.timeout,
        )

    def delete(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    )-> Response:
        return requests.delete(
            url=self._build_url(path),
            params=params,
            headers=headers,
            timeout=self.timeout,
        )