from ..models import User
from werkzeug.security import generate_password_hash
from fastapi.exceptions import HTTPException
from fastapi import status
from app.database import Session, engine
from ..schemas import SignupResponseModel


async def signup(user):
    session = Session(bind=engine)
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    new_user = User(
        email=user.email,
        password=generate_password_hash(user.password),
        name=user.name,
        phone=user.phone,
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    new_user_data = SignupResponseModel(
        email=new_user.email,
        name=new_user.name,
        phone=new_user.phone,
    )

    return new_user_data
