import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.core.settings import settings

Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    uuid_token = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4)

    audios = relationship('AudioModel', backref='user')


class AudioModel(Base):
    __tablename__ = 'audios'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file = Column(String)
    user_id = Column(ForeignKey('users.id'), nullable=False)

    @property
    def url(self):
        # Возвращает ссылку для скачивания.
        return f'{settings.DOWNLOAD_URL}?id={self.id}&user={self.user_id}'
