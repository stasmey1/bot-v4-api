from typing import List, TypeVar, Generic, Type

from pydantic import BaseModel
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from .database import Base

ORM = TypeVar("ORM", bound=Base)


class BaseDAO(Generic[ORM]):
    model: Type[ORM]

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get(self, id: int) -> ORM | None:
        query = select(self.model).filter_by(id=id)
        result = await self._session.execute(query)

        return result.scalar_one_or_none()

    async def get_list(self) -> List[ORM]:
        query = select(self.model)
        result = await self._session.execute(query)

        return result.scalars().all()

    async def create(self, data: BaseModel) -> ORM:
        values_dict = data.model_dump(exclude_unset=True)
        new_instance = self.model(**values_dict)
        self._session.add(new_instance)
        await self._session.flush()

        return new_instance

    async def update(self, id: int, data: BaseModel) -> ORM:
        raise NotImplementedError()

    async def delete(self, id: int):
        query = sqlalchemy_delete(self.model).filter(self.model == id)
        result = await self._session.execute(query)
        await self._session.flush()

        return result.rowcount
