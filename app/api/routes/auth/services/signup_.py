from ..models import User
from sqlalchemy.orm.session import Session
from werkzeug.security import generate_password_hash
from fastapi.exceptions import HTTPException
from fastapi import status
from ..schemas import SignupResponseModel, SignupRequestModel


def signup_(user: SignupRequestModel, session: Session):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    new_user = User(
        email=user.email,
        password=generate_password_hash(user.password),
        name=user.name,
        phone=user.phone,
    )
    session.add(new_user)
    new_user_data = SignupResponseModel(**new_user.__dict__)
    return new_user_data

