from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from db.models import Moderator
from db.schemas import ModeratorData

from db.repositories.base import BaseRepository


class ModeratorRepo(BaseRepository[Moderator, ModeratorData]):
    # NOTE: Here will special methods for ModeratorRepo(for example add_ad_for_moderate)
    model = Moderator

    @classmethod
    async def get_all(cls, session: AsyncSession) -> Sequence[Moderator]:
        query = select(cls.model).options(selectinload(Moderator.in_moderating))
        res = await session.execute(query)
        return res.scalars().all()

    @classmethod
    async def get_ids(cls, session: AsyncSession) -> Sequence[int]:
        res = await session.execute(select(cls.model.telegram_id))
        return res.scalars().all()

