from pydantic import BaseModel, ConfigDict, Field, model_validator

from typing import Self

from services.university.models.grade_request import MAX_GRADE, MIN_GRADE

class GradeStatsResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    count: int = Field(ge=0)
    min: int | None = Field(defailt=None, ge=MIN_GRADE, le=MAX_GRADE)
    max: int | None = Field(defailt=None, ge=MIN_GRADE, le=MAX_GRADE)
    avg: float | None = Field(defailt=None, ge=MIN_GRADE, le=MAX_GRADE)

    @model_validator(mode="after")
    def validate_stats_consistency(self) -> Self:
        if self.count == 0:
            if self.min is not None or self.max is not None or self.avg is not None:
                raise ValueError(
                    "Empty stats must have min, max or avg equal to None"
                )
            return self

        if self.min is None or self.max is None or self.avg is None:
            raise ValueError(
                "Non-empty stats must have min, max and avg values"
            )
        return self
