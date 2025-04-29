from sqlalchemy.orm import Mapped, mapped_column

from app.dao.database import Base


class MotivationPicture(Base):
    __tablename__ = "motivation_picture"
    __table_args__ = {"schema": "materials"}

    link: Mapped[str] = mapped_column(nullable=False)
