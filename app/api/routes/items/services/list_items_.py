from ..models import Item
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session


def list_items_(authorize: AuthJWT, session: Session, limit: int, offset: int):
    return session.query(Item).order_by(Item.id.desc()).limit(limit).offset(offset).all()
