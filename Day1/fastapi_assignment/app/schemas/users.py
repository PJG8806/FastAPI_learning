from pydantic import BaseModel, PositiveInt
from typing import Literal

class UserData(BaseModel):
    username: str
    age: int
    gender: Literal["male","female"]

class UserSelect(BaseModel):
    username: str | None = None
    age: PositiveInt | None = None # 1 이상의 정수만 받는다
    gender: Literal["male","female"] | None = None
    model_config = {"extra": "forbid"}