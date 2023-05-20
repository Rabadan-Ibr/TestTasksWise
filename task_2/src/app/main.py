from fastapi import FastAPI

from .routers.audios import audio_router
from .routers.users import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(audio_router)
