from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_session
from ..schemas.users import UserCreate, UserToken
from ..services.users import UserService

user_router = APIRouter(
    prefix='/users',
    tags=['users']
)


@user_router.get('/{user_id}', response_model=UserToken)
def get_user(
        user_id: int,
        service: UserService = Depends(),
        db: Session = Depends(get_session),
):
    user = service.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@user_router.post('/', response_model=UserToken)
def create_user(
        data: UserCreate,
        service: UserService = Depends(),
        db: Session = Depends(get_session),
):
    result = service.create(db, data.dict())
    return result
