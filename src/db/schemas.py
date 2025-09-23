# Схемы для таблиц sqlalchemy

from pydantic import BaseModel



class ModeratorData(BaseModel):
    telegram_id: int
    first_name: str|None
    last_name: str|None
    username: str|None
    
    in_moderating: list["AdData"] = []

class AdData(BaseModel):
    title: str
    description: str
    link: str # Link to project
    is_moderating: bool # Moderation status

    moderator: ModeratorData|None = None
