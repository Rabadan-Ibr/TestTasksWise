from datetime import datetime

from pydantic import BaseModel


class Question(BaseModel):
    id: int
    question: str
    answer: str
    date_created: datetime

    class Config:
        orm_mode = True


class QuestionParse(BaseModel):
    id: int
    question: str
    answer: str


class QuestionCreate(BaseModel):
    questions_num: int
