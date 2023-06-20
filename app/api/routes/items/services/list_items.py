from ..models import Item
from fastapi import HTTPException, status


async def list_items(authorize, session):
    try:
        authorize.jwt_required()
        items = session.query(Item).all()
        return items
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized"
        )
