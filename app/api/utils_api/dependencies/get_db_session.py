from sqlalchemy.orm.session import Session
from app.database import Session


def get_db_session():
    with Session() as s:
        with s.begin():
            yield s
            s.commit()
