from ..models import Item
from fastapi.exceptions import HTTPException
from fastapi import status


async def get_item(item_id: int, authorize, session):
    try:
        authorize.jwt_required()
        db_item = session.query(Item).filter(Item.id == item_id).first()

        if db_item:
            item_data = {
                "id": db_item.id,
                "title": db_item.title,
                "description": db_item.description,
            }
            return item_data

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e
        )