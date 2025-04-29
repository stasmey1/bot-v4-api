from sqlalchemy.orm import Mapped, mapped_column

from app.dao.database import Base


class Users(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "profiles"}  # Указываем схему profiles

    name: Mapped[str] = mapped_column(nullable=False)  # Указываем mapped_column
    telegram_id: Mapped[int | None] = mapped_column(default=None)  # Указываем mapped_column
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
