from sqlalchemy.orm import Mapped, mapped_column

from app.dao.database import Base


class CategoryVideo(Base):
    __tablename__ = "category_video"
    __table_args__ = {"schema": "materials"}

    name: Mapped[str] = mapped_column(nullable=False)
