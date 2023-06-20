from ..models import Item
from app.api.routes.auth.models import User
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi import status
from ..schemas import UpdateItemRequestModel, UpdateItemResponseModel


def update_item_(item_id: int, item: UpdateItemRequestModel, authorize: AuthJWT, session: Session):
    db_item = session.query(Item).filter(Item.id == item_id).first()

    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()

    if db_item is not None and db_item.owner_id != db_user.id:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Item does not belong to current user")

    elif db_item is not None:
        db_item.title = item.title
        db_item.description = item.description

    updated_item_data = UpdateItemResponseModel(**db_item.__dict__)
    return updated_item_data
