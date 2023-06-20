from ..models import Item
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session


def list_items_(authorize: AuthJWT, session: Session):
    return session.query(Item).all()
