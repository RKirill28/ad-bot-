# Схемы для таблиц sqlalchemy

from pydantic import BaseModel, ConfigDict


class ModeratorData(BaseModel):
    telegram_id: int
    first_name: str | None
    last_name: str | None
    username: str | None

    in_moderating: list["AdData"] = []
    model_config = ConfigDict(from_attributes=True)


class AdData(BaseModel):
    title: str
    description: str
    link: str  # Link to project
    is_moderating: bool  # Moderation status

    # moderator: ModeratorData | None = None
    model_config = ConfigDict(from_attributes=True)
