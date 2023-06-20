from app.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(Text)
    name = Column(String)
    phone = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    items = relationship('Item', back_populates='owner',)  # Define the relationship here

    def __repr__(self):
        return f"<User {self.name}>"
