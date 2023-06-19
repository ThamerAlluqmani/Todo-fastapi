from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = 'd3a4bca378f77879a6c1229be08b269c4d8d4f52438c170732950944ee95492e'
    authjwt_algorithm: str = 'HS256'
