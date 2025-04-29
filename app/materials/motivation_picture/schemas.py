from pydantic import BaseModel


class CreateMotivationPictureSchema(BaseModel):
    link: str


class UpdateMotivationPictureSchema(CreateMotivationPictureSchema):
    ...


class OutMotivationPictureSchema(CreateMotivationPictureSchema):
    id: int
