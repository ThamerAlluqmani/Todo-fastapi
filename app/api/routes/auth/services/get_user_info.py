from ..models import User
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from fastapi.exceptions import HTTPException
from fastapi import status
from app.database import Session, engine

session = Session(bind=engine)


async def get_user_info(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        current_user_email = Authorize.get_jwt_subject()

        session = Session(bind=engine)
        db_user = session.query(User).filter(User.email == current_user_email).first()
        session.close()

        if db_user:
            user_data = {
                "email": db_user.email,
                "name": db_user.name,
                "phone": db_user.phone,
            }
            return user_data

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
