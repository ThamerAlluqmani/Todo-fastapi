from app.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='items')

    def __repr__(self):
        return f"<User {self.title}>"