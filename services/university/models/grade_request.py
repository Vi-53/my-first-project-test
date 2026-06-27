from pydantic import BaseModel, ConfigDict, Field


MIN_GRADE = 2
MAX_GRADE = 5


class GradeRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=MIN_GRADE, le=MAX_GRADE)
