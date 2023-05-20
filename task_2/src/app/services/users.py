from typing import Optional
from uuid import UUID

from sqlalchemy.orm import Session

from ..crud import BaseCRUD
from ..tables import UserModel


class UserService(BaseCRUD):
    _model = UserModel

    def get_with_token(
            self,
            db: Session,
            user_id: int,
            user_token: UUID,
    ) -> Optional[UserModel]:
        # Возвращает пользователя с заданным uuid_token, если они совпадают.
        user = self.get_by_id(db, user_id)
        if user is None or user.uuid_token != user_token:
            return None
        return user
