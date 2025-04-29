from sqlalchemy.orm import Mapped, mapped_column

from app.dao.database import Base


class CategoryMaterials(Base):
    __tablename__ = "category_materials"
    __table_args__ = {"schema": "materials"}

    name: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True)
