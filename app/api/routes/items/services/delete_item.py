from ..models import Item
from fastapi.exceptions import HTTPException
from fastapi import status


def delete_item(item_id: int, authorize, session):
    try:
        authorize.jwt_required()
        db_item = session.query(Item).filter(Item.id == item_id).first()

        if db_item is not None:
            session.delete(db_item)
            session.commit()
            session.close()
            return {
                "message": "Item deleted successfully"
            }

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e
        )
