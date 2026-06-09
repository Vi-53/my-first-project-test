from requests import Response


def test_services_openapi_available(auth_api) -> None:
    response: Response = auth_api.get("/openapi.json")

    assert response.status_code == 200, response.text

    body = response.json()

    assert "openapi" in body
    assert "paths" in body

def test_university_service_openapi_available(university_api) -> None:
    response: Response = university_api.get("/openapi.json")

    assert response.status_code == 200, response.text

    body = response.json()

    assert "openapi" in body
    assert "paths" in body