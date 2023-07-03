from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT  # type: ignore
from app.api.routes.auth.models import User
from fastapi import HTTPException, status


def delete_user_(authorize: AuthJWT, session: Session):
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()
    if db_user is not None:
        session.delete(db_user)
        return {"message": "User deleted successfully"}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
