from pydantic import BaseModel,Field
from enum import Enum

class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'

class CreatUser(BaseModel):
    username: str
    age: int
    gender: GenderEnum

class UpdateUser(BaseModel):
    username: str
    age: int

class UserFilter(BaseModel):
    model_config = ["extra:forbid"] # 정의되지 않은 필드 차단
    username: str
    age: int = Field(gt=0)
    gender: GenderEnum
