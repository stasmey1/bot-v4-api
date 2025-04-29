from pydantic import BaseModel


class CreateComplimentsSchema(BaseModel):
    text: str


class UpdateComplimentsSchema(CreateComplimentsSchema):
    ...


class OutComplimentsSchema(CreateComplimentsSchema):
    id: int
