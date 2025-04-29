from pydantic import BaseModel


class CreateCategoryMaterialsSchema(BaseModel):
    name: str


class UpdateCategoryMaterialsSchema(CreateCategoryMaterialsSchema):
    ...


class OutCategoryMaterialsSchema(CreateCategoryMaterialsSchema):
    id: int
    is_active: bool
