from typing import Any


def assert_status_code(response, expected_status_code: int) -> None:
    assert response.status_code == expected_status_code, (
        f"Wrong status code "
        f"Actual: {response.status_code}, expected: {expected_status_code} "
        f"Response body: {response.text}"
    )

def format_assert_value(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump()
    return value

def assert_equal(
    actual: Any,
    expected: Any,
    message: str = "Value are not equal",
) -> None:
    assert actual == expected, (
        f"{message} "
        f"Actual: {format_assert_value(actual)}, "
        f"expected: {format_assert_value(expected)} "

    )