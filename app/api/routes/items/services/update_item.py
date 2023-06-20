from ..models import Item
from fastapi.exceptions import HTTPException
from fastapi import status


async def update_item(item_id: int, item, authorize, session):
    try:
        authorize.jwt_required()
        db_item = session.query(Item).filter(Item.id == item_id).first()

        if db_item:
            db_item.title = item.title
            db_item.description = item.description
            session.commit()
            session.close()
            return {
                "title": db_item.title,
                "description": db_item.description,
            }

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e
        )
