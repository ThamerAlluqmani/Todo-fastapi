from ..models import Item
from sqlalchemy.orm.session import Session
from fastapi_jwt_auth import AuthJWT
from ..schemas import UpdateItemRequestModel, UpdateItemResponseModel


def update_item_(item_id: int, item: UpdateItemRequestModel, authorize: AuthJWT, session: Session):
    db_item = session.query(Item).filter(Item.id == item_id).first()

    if db_item is not None:
        db_item.title = item.title
        db_item.description = item.description

    updated_item_data = UpdateItemResponseModel(**db_item.__dict__)
    return updated_item_data
