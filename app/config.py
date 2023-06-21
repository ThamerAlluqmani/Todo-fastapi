from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = 'd3a4bca378f77879a6c1229be08b269c4d8d4f52438c170732950944ee95492e'
    authjwt_algorithm: str = 'HS256'
    CELERY_BROKER_URL: str = 'redis://127.0.0.1:6379/0'
    CELERY_RESULT_BACKEND: str = 'redis://127.0.0.1:6379/0'
