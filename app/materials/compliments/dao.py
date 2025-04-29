from app.dao.base import BaseDAO
from app.materials.compliments.models import Compliments
from app.materials.compliments.schemas import CreateComplimentsSchema


class ComplimentsDAO(BaseDAO):
    model = Compliments
    create_schema = CreateComplimentsSchema
