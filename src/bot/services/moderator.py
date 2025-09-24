from db.repositories.moderator_repo import ModeratorRepo
from db.schemas import ModeratorData

from sqlalchemy.ext.asyncio import AsyncSession


async def get_moderators_list(session: AsyncSession) -> list[ModeratorData]:
    from_db = await ModeratorRepo.get_all(session)
    new_data = [
        ModeratorData.model_validate(data, from_attributes=True) for data in from_db
    ]
    return new_data
