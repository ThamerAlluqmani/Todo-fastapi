from typing import Union
from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT
from app.config import Settings
from app.api.routes.auth.router import auth_router

app = FastAPI()


@AuthJWT.load_config
def get_config():
    return Settings()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(auth_router, prefix="/auth", tags=["auth"])
