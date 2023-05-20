from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_session
from ..schemas.questions import Question, QuestionCreate
from ..services.questions import QuestionsService

question_router = APIRouter(
    prefix='/question',
    tags=['question'],
)


@question_router.get('/', response_model=list[Question])
def get_questions(
        db: Session = Depends(get_session),
        service: QuestionsService = Depends(),
):
    response = service.get_all(db)
    return response


@question_router.post('/', response_model=Optional[Question])
def create_question(
        data: QuestionCreate,
        db: Session = Depends(get_session),
        service: QuestionsService = Depends(),
):
    response: Optional[Question] = service.get_last_question(db)
    count: int = data.questions_num
    while count > 0:
        questions = service.get_questions(count)
        for question in questions:
            if service.get_by_id(db, question.id) is None:
                service.create(db, question.dict())
                count -= 1
    return response
