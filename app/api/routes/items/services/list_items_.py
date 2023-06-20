from ..models import Item
from app.api.routes.auth.models import User
from fastapi_jwt_auth import AuthJWT
from sqlalchemy.orm import Session


def list_items_(authorize: AuthJWT, session: Session, limit: int, offset: int):
    # list all items by owner id and order by id desc
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()

    return session.query(Item).filter(Item.owner_id == db_user.id).order_by(Item.id.desc()).limit(limit).offset(offset).all()