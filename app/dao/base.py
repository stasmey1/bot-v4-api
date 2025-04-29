from typing import List, TypeVar, Generic, Type

from pydantic import BaseModel
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from .database import Base

ORM = TypeVar("ORM", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)


class BaseDAO(Generic[ORM, CreateSchemaType]):
    model: Type[ORM]
    create_schema: Type[CreateSchemaType] = None

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, id: int) -> ORM | None:
        query = select(self.model).where(self.model.id == id)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def get_list(self) -> List[ORM]:
        query = select(self.model)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def create(self, data: dict) -> ORM:
        create_data = self.create_schema(**data)
        new_instance = self.model(**create_data.model_dump())
        self._session.add(new_instance)
        await self._session.flush()

        return new_instance

    async def update(self, id: int, data: BaseModel) -> ORM:
        raise NotImplementedError()

    async def delete(self, id: int) -> ORM:
        orm = await self._session.get(self.model, id)
        await self._session.delete(orm)

        return orm
