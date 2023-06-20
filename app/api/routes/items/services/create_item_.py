from ..models import Item
from app.api.routes.auth.models import User
from fastapi_jwt_auth import AuthJWT
from ..schemas import CreateItemResponseModel, CreateItemRequestModel
from sqlalchemy.orm import Session


def create_item_(item: CreateItemRequestModel, authorize: AuthJWT, session: Session):
    current_user_email = authorize
    db_user = session.query(User).filter(User.email == current_user_email).first()
    new_item = Item(
        title=item.title,
        description=item.description,
        owner_id=db_user.id
    )
    session.add(new_item)
    new_item_data = CreateItemResponseModel(**new_item.__dict__)
    return new_item_data
