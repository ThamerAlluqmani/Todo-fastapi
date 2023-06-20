from ..models import Item
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT


def delete_item_(item_id: int, authorize: AuthJWT, session: Session):
    db_item = session.query(Item).filter(Item.id == item_id).first()

    if db_item is not None:
        session.delete(db_item)
        return {
            "message": "Item deleted successfully"
        }
    return {
        "message": "Item not found"
    }
