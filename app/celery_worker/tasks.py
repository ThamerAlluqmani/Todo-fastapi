from .app import app
from app.api.utils_api.dependencies import get_db_session
from app.api.routes.items.models import Item
from sqlalchemy.orm.session import Session


@app.task
def change_item_status_(item_id: int):
    session: Session = next(get_db_session())
    db_item = session.query(Item).filter(Item.id == item_id).first()
    if db_item is not None:
        db_item.is_done = True
        session.commit()

