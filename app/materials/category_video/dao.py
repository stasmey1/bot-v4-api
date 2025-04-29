from app.dao.base import BaseDAO
from app.materials.category_video.models import CategoryVideo
from app.materials.category_video.schemas import CreateCategoryVideoSchema


class CategoryVideoDAO(BaseDAO):
    model = CategoryVideo
    create_schema = CreateCategoryVideoSchema
