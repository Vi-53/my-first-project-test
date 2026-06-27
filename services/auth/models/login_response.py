from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class LoginResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    access_token: str = Field(min_length=1)
    token_type: Literal["Bearer"]
