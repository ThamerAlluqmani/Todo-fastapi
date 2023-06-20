from sqlalchemy.orm.session import Session

from app.database import Session


def get_db_session():
    session: Session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
