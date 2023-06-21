from celery import Celery
from app.config import Settings

settings = Settings()
app = Celery(
    "tasks",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)