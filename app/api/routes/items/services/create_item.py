from ..models import Item
from app.database import Session, engine
from fastapi import HTTPException, status
from ..schemas import CreateResponseModel


async def create_item(item, authorize, session):
    try:
        authorize.jwt_required()
        new_item = Item(
            title=item.title,
            description=item.description,
            owner_id=item.owner_id
        )
        session.add(new_item)
        session.commit()
        session.refresh(new_item)
        new_user_data = CreateResponseModel(
            title=new_item.title,
            description=new_item.description,
        )

        return new_user_data
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized"
        )
