from ..models import Item
from fastapi.exceptions import HTTPException
from fastapi import status


def get_item_(item_id: int, authorize, session):
    db_item = session.query(Item).filter(Item.id == item_id).first()

    if db_item is not None:
        item_data = {
            "id": db_item.id,
            "title": db_item.title,
            "description": db_item.description,
        }
        return item_data

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")