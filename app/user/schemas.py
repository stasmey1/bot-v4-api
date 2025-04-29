from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    telegram_id: int | None = None
    is_active: bool = True
    is_admin: bool = False


class UserOutSchema(UserCreateSchema):
    id: int
