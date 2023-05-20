from pydantic import BaseModel
from pydantic.types import UUID


class UserCreate(BaseModel):
    name: str


class UserToken(BaseModel):
    id: int
    uuid_token: UUID

    class Config:
        orm_mode = True
