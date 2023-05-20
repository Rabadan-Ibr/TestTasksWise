import os
import shutil
import subprocess
import uuid
from pathlib import Path
from typing import Optional

from fastapi import UploadFile
from sqlalchemy.orm import Session

from ..crud import BaseCRUD
from ..tables import AudioModel

from ..core.settings import settings


class AudioService(BaseCRUD):
    _model = AudioModel

    def convert_to_mp3(self, file: UploadFile, destination: Path):
        # Создание пути для временного файла.
        temp = settings.TEMP_DIR / f'{uuid.uuid1()}{file.filename[-4:]}'

        if not settings.TEMP_DIR.exists():
            settings.TEMP_DIR.mkdir()

        # Запись из памяти во временный файл.
        with temp.open('ab') as f:
            shutil.copyfileobj(file.file, f)

        if not destination.exists():
            destination.mkdir(parents=True)

        # Создание пути для файла и конвертация в mp3.
        file_name = destination / f'{uuid.uuid4()}.mp3'
        subprocess.run([
            'ffmpeg',
            '-i', temp,
            '-ar', '44100',
            '-ac', '2',
            '-b:a', '192k',
            file_name,
        ])
        # Удаление временного файла.
        temp.unlink()
        return file_name if file_name.exists() else None

    def get_audio(
            self,
            db: Session,
            audio_id: uuid.UUID,
            user_id: int,
    ) -> Optional[AudioModel]:
        # Получение записи из базы данных по id и user_id.
        model = self._get_model()
        audio = db.query(model).filter_by(id=audio_id, user_id=user_id).first()
        return audio

    def delete(self, db: Session, db_obj: AudioModel) -> None:
        # Удаление файла перед удалением записи.
        os.remove(db_obj.file_path)
        super().delete(db, db_obj)
