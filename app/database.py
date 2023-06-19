from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgresql://root:root@localhost:5432/Todo_db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
