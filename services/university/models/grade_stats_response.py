from typing import Self

from pydantic import BaseModel, ConfigDict, Field, model_validator

from services.university.models.grade_request import MAX_GRADE, MIN_GRADE


class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)
    min: int | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE)
    max: int | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE)
    avg: float | None = Field(default=None, ge=MIN_GRADE, le=MAX_GRADE)

    @model_validator(mode="after")
    def validate_stats_consistency(self) -> Self:
        stats_values = [
            self.min,
            self.max,
            self.avg,
        ]
        if self.count == 0:
            if any(value is not None for value in stats_values):
                raise ValueError(
                    "Empty stats must have min, max and avg equal to None"
                )
            return self

        if any(value is None for value in stats_values):
            raise ValueError(
                "Non-empty stats must have min, max and avg values"
            )

        if self.min > self.max:
            raise ValueError(
                f"Stats min must be than or equal to max"
                f"Actual min: '{self.min}', max: 'self.max'"
            )
        return self
