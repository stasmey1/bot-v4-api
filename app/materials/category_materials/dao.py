from app.dao.base import BaseDAO
from app.materials.category_materials.models import CategoryMaterials
from app.materials.category_materials.schemas import CreateCategoryMaterialsSchema


class CategoryMaterialsDAO(BaseDAO):
    model = CategoryMaterials
    create_schema = CreateCategoryMaterialsSchema
