from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    name: str


class OutUserSchema(CreateUserSchema):
    id: int
    telegram_id: int | None = None
    is_active: bool
    is_admin: bool


class UpdateUserSchema(BaseModel):
    name: str
    telegram_id: int | None = None
    is_active: bool = True
    is_admin: bool = False
