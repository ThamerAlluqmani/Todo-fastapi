from sqlalchemy import select

from .app import app
from sqlalchemy.orm.session import Session
from app.api.utils_api.dependencies import get_db_session
from app.api.routes.items.models import Item


@app.task
def change_item_status_(item_id: int):
    session: Session = next(get_db_session())
    stmt = select(Item).where(Item.id == item_id)
    db_item = session.execute(stmt).scalar_one_or_none()
    if db_item is None:
        return "Item not found"

    db_item.is_done = True
    session.commit()
