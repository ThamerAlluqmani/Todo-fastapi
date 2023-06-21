from ..models import Item
from app.api.routes.auth.models import User
from fastapi.exceptions import HTTPException
from fastapi import status


def get_item_(item_id: int, authorize, session):
    db_item = session.query(Item).filter(Item.id == item_id).first()
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()
    if db_item is not None and db_item.owner_id != db_user.id:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Item does not belong to current user")

    elif db_item is not None:
        item_data = {
            "id": db_item.id,
            "title": db_item.title,
            "description": db_item.description,
            "is_done": db_item.is_done,
        }
        return item_data

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")