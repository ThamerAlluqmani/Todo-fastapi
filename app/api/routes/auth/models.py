from app.database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

server_default = "false"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()
    name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    items: Mapped[str] = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"<User {self.name}>"
