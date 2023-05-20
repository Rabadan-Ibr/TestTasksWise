import requests
from sqlalchemy.orm import Session

from ..core.settings import settings
from ..crud import BaseCRUD
from ..schemas.questions import QuestionParse
from ..tables import Questions


class QuestionsService(BaseCRUD):
    _model = Questions

    def get_last_question(self, db: Session) -> Questions | None:
        return db.query(self._get_model()).order_by(
            self._get_model().date_created.desc()
        ).first()

    def get_questions(self, count: int) -> list[QuestionParse]:
        response = requests.get(
            f'{settings.QUESTIONS_SERVICE_URL}{count}',
        )
        return [QuestionParse(**obj) for obj in response.json()]
