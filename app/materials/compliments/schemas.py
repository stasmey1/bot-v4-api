from pydantic import BaseModel


class CreateComplimentsSchema(BaseModel):
    text: str


class UpdateUserSchema(CreateComplimentsSchema):
    ...


class OutComplimentsSchema(CreateComplimentsSchema):
    id: int
