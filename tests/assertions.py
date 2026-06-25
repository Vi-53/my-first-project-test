import pytest

from services.university.models.grade_stats_response import GradeStatsResponse


def assert_status_code(response, expected_status_code: int) -> None:
    assert response.status_code == expected_status_code, (
        f"Wrong status code. "
        f"Actual: '{response.status_code}', expected: '{expected_status_code}'. "
        f"Response body: '{response.text}'"
    )


def assert_response_has_field(
        body: dict,
        field_name: str,
) -> None:
    assert field_name in body, (
        f"Required field is missing. "
        f"Field: '{field_name}'. "
        f"Actual response body: '{body}'."
    )


def assert_json_content_type(response) -> None:
    actual_content_type = response.headers["content-type"]
    expected_content_type = "application/json"

    assert actual_content_type.startswith(expected_content_type), (
        f"Wrong content-type. "
        f"Actual: '{actual_content_type}', "
        f"expected starts with: '{expected_content_type}'."
    )


def assert_stats_equal(
        actual: GradeStatsResponse,
        expected: dict[str, int | float | None],
) -> None:
    assert actual.count == expected["count"], (
        f"Wrong stats count. "
        f"Actual: '{actual.count}', expected: '{expected['count']}'."
    )

    assert actual.min == expected["min"], (
        f"Wrong stats min. "
        f"Actual: '{actual.min}', expected: '{expected['min']}'."
    )

    assert actual.max == expected["max"], (
        f"Wrong stats max. "
        f"Actual: '{actual.max}', expected: '{expected['max']}'."
    )

    if expected["avg"] is None:
        assert actual.avg is None, (
            f"Wrong stats avg. "
            f"Actual: '{actual.avg}', expected: 'None'."
        )
    else:
        assert actual.avg == pytest.approx(expected["avg"]), (
            f"Wrong stats avg. "
            f"Actual: '{actual.avg}', expected approximately: '{expected['avg']}'."
        )


def assert_response_field_value(
        body: dict,
        field_name: str,
        expected_value,
) -> None:
    actual_value = body.get(field_name)

    assert actual_value == expected_value, (
        f"Wrong field value. "
        f"Field: '{field_name}'. "
        f"Actual: '{actual_value}', expected: '{expected_value}'. "
        f"Actual response body: '{body}'."
    )


def assert_response_field_type(
        body: dict,
        field_name: str,
        expected_type: type,
) -> None:
    actual_value = body.get(field_name)

    assert isinstance(actual_value, expected_type), (
        f"Wrong field type. "
        f"Field: '{field_name}'. "
        f"Actual type: '{type(actual_value)}', expected: '{expected_type}'. "
        f"Actual value: '{actual_value}'. "
        f"Actual response body: '{body}'."
    )
