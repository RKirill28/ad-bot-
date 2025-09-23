from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Type, Sequence

from db import Base


class BaseRepository[T: Base, M: BaseModel]:
    model: Type[T]

    @classmethod
    def create(cls, session: AsyncSession, schema: M) -> T:
        obj = cls.model(**schema.model_dump())
        session.add(obj)
        return obj

    @classmethod
    async def get_by_id(cls, session: AsyncSession, id: int) -> T | None:
        return await session.get(cls.model, id)

    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[T]:
        res = await session.execute(select(cls.model))
        return res.scalars().all()

    @classmethod
    async def remove(cls, session: AsyncSession, id: int) -> None:
        obj = await session.get(cls.model, id)
        if obj:
            await session.delete(obj)
