from pydantic import BaseModel


class CreateCategoryVideoSchema(BaseModel):
    name: str


class UpdateCategoryVideoSchema(CreateCategoryVideoSchema):
    ...


class OutCategoryVideoSchema(CreateCategoryVideoSchema):
    id: int
