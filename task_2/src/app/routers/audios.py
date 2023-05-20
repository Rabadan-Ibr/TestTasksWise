from pathlib import Path
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from ..core.settings import settings
from ..database import get_session
from ..schemas.audios import UploadResponse
from ..services.audios import AudioService
from ..services.users import UserService

audio_router = APIRouter(tags=['audio'])


@audio_router.post('/upload', response_model=UploadResponse)
def upload_audio(
        user_id: Annotated[int, Form()],
        user_token: Annotated[UUID,  Form()],
        file: UploadFile,
        user_service: UserService = Depends(),
        audio_service: AudioService = Depends(),
        db: Session = Depends(get_session),
):
    # Получение пользователя из базы данных.
    user = user_service.get_with_token(db, user_id, user_token)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    # Проверка расширения файла.
    if file.filename[-4:].lower() != '.wav':
        raise HTTPException(status_code=400, detail='File must be .wav')

    # Конвертация в .mp3 и сохранение файла.
    file_destination = settings.STATIC_DIR / 'audio' / str(user.id)

    mp3_file = audio_service.convert_to_mp3(file, file_destination)
    if mp3_file is None:
        raise HTTPException(status_code=500, detail='Error converting file')

    # Создание записи  в базе данных и возврат ссылки для скачивания.
    data = {
        'id': mp3_file.name[:-4],
        'file': str(mp3_file),
        'user_id': user.id,
    }
    return audio_service.create(db, data)


@audio_router.get('/record',)
def get_audio(
        id: UUID,
        user: int,
        audio_service: AudioService = Depends(),
        db: Session = Depends(get_session),
):
    # Получение записи из базы данных.
    audio = audio_service.get_audio(db, id, user)
    if audio is None:
        raise HTTPException(status_code=404, detail='Record not found')

    if not Path(audio.file).exists():
        raise HTTPException(status_code=500, detail='File not found')

    return FileResponse(
        audio.file,
        media_type='multipart/form-data',
        filename=f'{audio.id}.mp3',
    )
