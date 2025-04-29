from app.dao.base import BaseDAO
from app.user.models import Users
from app.user.schemas import CreateUserSchema


class UsersDAO(BaseDAO):
    model = Users
    create_schema = CreateUserSchema
