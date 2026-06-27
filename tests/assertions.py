import pytest

from services.university.models.grade_stats_response import GradeStatsResponse


class SoftAssert:
    def __init__(self):
        self.errors: list[str] = []

    def check_equal(self, actual, expected, message: str) -> None:
        if actual != expected:
            self.errors.append(
                f"{message} Actual: {actual}, Expected: {expected}"
            )
    def check_approx(self, actual, expected, message: str) -> None:
        if actual != pytest.approx(expected):
            self.errors.append(
                f"{message} Actual: {actual}, Expected approximately: {expected}"
            )
    def assert_all(self) -> None:
        assert not self.errors, (
            "soft assert failed:\n"
            + "\n".join(
                f"{index}. {error}"
                for index, error in enumerate(self.errors, start=1)
            )
        )

def assert_status_code(response, expected_status_code: int) -> None:
    assert response.status_code == expected_status_code, (
        f"Wrong status code. "
        f"Actual: '{response.status_code}', expected: '{expected_status_code}'. "
        f"Response body: '{response.text}'"
    )

def assert_stats_equal(
        actual: GradeStatsResponse,
        expected: GradeStatsResponse,
) -> None:
    soft_assert = SoftAssert()

    soft_assert.check_equal(
        actual=actual.count,
        expected=expected.count,
        message="Wrong stats count",
    )

    soft_assert.check_equal(
        actual=actual.min,
        expected=expected.min,
        message="Wrong stats min",
    )

    soft_assert.check_equal(
        actual=actual.max,
        expected=expected.max,
        message="Wrong stats max",
    )

    if expected.avg is None:
        soft_assert.check_equal(
            actual=actual.avg,
            expected=None,
            message="Wrong stats avg",
        )
    else:
        soft_assert.check_approx(
            actual=actual.avg,
            expected=expected.avg,
            message="Wrong stats avg",
        )

        soft_assert.assert_all()
