import uuid
from datetime import datetime
from decimal import Decimal
from typing import Annotated
from sqlalchemy import Integer, inspect
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine, AsyncSession

from app.config import settings

engine = create_async_engine(url=settings.DATABASE_ASYNC_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    def to_dict(self, exclude_none: bool = False) -> dict:
        """
        Преобразует объект модели в словарь.

        Args:
            exclude_none (bool): Исключать ли None значения из результата

        Returns:
            dict: Словарь с данными объекта
        """
        result = {}

        for column in inspect(self.__class__).columns:
            value = getattr(self, column.key)

            # Преобразование специальных типов данных
            if isinstance(value, datetime):
                value = value.isoformat()
            elif isinstance(value, Decimal):
                value = float(value)
            elif isinstance(value, uuid.UUID):
                value = str(value)

            # Добавляем значение в результат
            if not exclude_none or value is not None:
                result[column.key] = value

        return result

    def __repr__(self) -> str:
        """Строковое представление объекта для удобства отладки."""
        return f"<{self.__class__.__name__}(id={self.id})>"
