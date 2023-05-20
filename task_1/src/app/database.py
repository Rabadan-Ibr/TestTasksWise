from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .core.settings import settings

DATABASE_URL: str = (
    f'postgresql://{settings.POSTGRES_USER}:'
    f'{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}/'
    f'{settings.POSTGRES_DB}'
)
engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
