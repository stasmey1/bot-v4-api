from sqlalchemy.orm import Mapped, mapped_column

from app.dao.database import Base


class Compliments(Base):
    __tablename__ = "compliment"
    __table_args__ = {"schema": "materials"}

    text: Mapped[str] = mapped_column(nullable=False)
