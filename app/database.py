from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://root:root@localhost:5432/TODO_FAST_API', echo=True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)