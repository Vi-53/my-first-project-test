from services.university.models.grade_stats_response import GradeStatsResponse


def assert_status_code(response, expected_status_code: int) -> None:
    assert response.status_code == expected_status_code, (
        f"Wrong status code"
        f"Actual: {response.status_code}, expected: {expected_status_code}"
        f"Response body: {response.text}"
    )

def assert_stats_equal(
        actual: GradeStatsResponse,
        expected: GradeStatsResponse,
) -> None:
    assert actual == expected, (
        f"Wrong grade stats"
        f"Actual: {actual.model_dump()}"
        f"Expected: {expected.model_dump()}"
    )
