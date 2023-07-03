from ..models import Item
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from app.api.routes.auth.models import User
from fastapi import HTTPException, status


def delete_item_(item_id: int, authorize: AuthJWT, session: Session):
    db_item = session.query(Item).filter(Item.id == item_id).first()
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()
    if db_item is not None and db_item.owner_id != db_user.id:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item does not belong to current user",
        )

    if db_item is not None:
        session.delete(db_item)
        return {"message": "Item deleted successfully"}
    return {"message": "Item not found"}
