from ..models import Item
from fastapi_jwt_auth import AuthJWT
from ..schemas import CreateItemResponseModel, CreateItemRequestModel
from sqlalchemy.orm import Session


def create_item_(item: CreateItemRequestModel, authorize: AuthJWT, session: Session):
    new_item = Item(
        title=item.title,
        description=item.description,
        owner_id=item.owner_id
    )
    session.add(new_item)
    new_item_data = CreateItemResponseModel(**new_item.__dict__)
    return new_item_data
