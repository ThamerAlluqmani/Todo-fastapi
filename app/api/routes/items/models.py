from app.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(Text, index=True)
    is_done = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='items')

    def __repr__(self):
        return f"<User {self.title}>"
