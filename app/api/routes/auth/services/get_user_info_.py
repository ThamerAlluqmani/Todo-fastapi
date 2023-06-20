from ..models import User
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm.session import Session
from fastapi_jwt_auth import AuthJWT


def get_user_info_(authorize: AuthJWT, session: Session):
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()

    if db_user is not None:
        user_data = {
            "email": db_user.email,
            "name": db_user.name,
            "phone": db_user.phone,
        }
        return user_data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")