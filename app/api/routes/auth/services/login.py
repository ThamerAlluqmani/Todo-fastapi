from ..models import User
from werkzeug.security import check_password_hash
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from fastapi import status
from app.database import Session, engine


async def login(user, authorize):
    session = Session(bind=engine)
    db_user = session.query(User).filter(User.email == user.email).first()
    if db_user and check_password_hash(db_user.password, user.password):
        access_token = authorize.create_access_token(subject=db_user.email)
        refresh_token = authorize.create_refresh_token(subject=db_user.email)
        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
        return jsonable_encoder(response)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
