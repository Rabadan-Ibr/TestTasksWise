from typing import Optional

from sqlalchemy.orm import Session

from app.tables import Base


class BaseCRUD:
    """
    Базовый CRUD класс
    Необходимо определить аргумент _model для класса
    """
    _model: Base = None

    def _get_model(self) -> 'BaseCRUD._model':
        if self._model is None:
            raise NotImplementedError('Need to set model')
        return self._model

    def get_all(self, db: Session) -> list['BaseCRUD._model']:
        return db.query(self._get_model()).all()

    def get_by_id(
            self, db: Session, id: int
    ) -> Optional['BaseCRUD._model']:
        return db.get(self._get_model(), id)

    def create(self, db: Session, obj_in: dict) -> 'BaseCRUD._model':
        db_obj = self._get_model()(**obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj: 'BaseCRUD._model') -> None:
        db.delete(db_obj)
        db.commit()
