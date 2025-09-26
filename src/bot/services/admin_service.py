from aiogram.types import ChatFullInfo
from sqlalchemy.ext.asyncio import AsyncSession

from db.repositories.moderator_repo import ModeratorRepo
from db.schemas import ModeratorData


class AlredyExists(Exception):
    """Ошибка указывающая на то, что объект в бд уже существует"""


async def add_moder(session: AsyncSession, user_info: ChatFullInfo) -> ModeratorData:
    user = ModeratorData(
        telegram_id=user_info.id,
        first_name=user_info.first_name,
        last_name=user_info.last_name,
        username=user_info.username,
    )
    ModeratorRepo.create(session, user)  # Добаляем модера в бд

    await session.commit()
    return user


async def delete_moder(session: AsyncSession, id: int) -> None:
    await ModeratorRepo.remove(session, id)
    await session.commit()
