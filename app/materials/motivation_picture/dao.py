from app.dao.base import BaseDAO
from app.materials.motivation_picture.models import MotivationPicture
from app.materials.motivation_picture.schemas import CreateMotivationPictureSchema


class MotivationPictureDAO(BaseDAO):
    model = MotivationPicture
    create_schema = CreateMotivationPictureSchema
