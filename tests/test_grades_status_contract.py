import pytest


def test_get_grades_stats_without_returns_403(grades_helper):
    response = grades_helper.get_stats()

    assert response.status_code == 403, response.text

    body = response.json()

    assert body["detail"] == "Access denied"

def test_get_grades_stats_success_response_contract(
        grades_helper,
        auth_headers,
):
    response = grades_helper.get_stats(headers=auth_headers)

    assert response.status_code == 200, response.text
    assert response.headers['Content-Type'].startswith('application/json')

    body = response.json()

    assert "count" in body
    assert "min" in body
    assert "max" in body
    assert "avg" in body

    assert isinstance(body["count"], int)

    if body["count"] == 0:
        assert body["min"] is None
        assert body["max"] is None
        assert body["avg"] is None
    else:
        assert isinstance(body["min"], int)
        assert isinstance(body["max"], int)
        assert isinstance(body["avg"], float | int)

@pytest.mark.parametrize(
    "param_name",
    [
        "student_id",
        "teacher_id",
        "group_id",
    ],
)
def test_get_grades_stats_with_invalid_id_returns_422(
        grades_helper,
        auth_headers,
        param_name,
):
    response = grades_helper.get_stats(
        params={param_name:"abs"},
        headers=auth_headers,
    )
    assert response.status_code == 422, response.text