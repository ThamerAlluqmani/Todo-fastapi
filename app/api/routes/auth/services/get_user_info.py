from ..models import User
from fastapi.exceptions import HTTPException
from fastapi import status


async def get_user_info(authorize, session):
    try:
        authorize.jwt_required()
        current_user_email = authorize.get_jwt_subject()

        db_user = session.query(User).filter(User.email == current_user_email).first()

        if db_user:
            user_data = {
                "email": db_user.email,
                "name": db_user.name,
                "phone": db_user.phone,
            }
            return user_data

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e
        )
