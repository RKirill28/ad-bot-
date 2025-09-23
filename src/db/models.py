from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'

class Moderator(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int]
    first_name: Mapped[str|None]
    last_name: Mapped[str|None]
    username: Mapped[str|None]
    
    in_moderating: Mapped[list["Ad"]] = relationship(back_populates="moderator")

class Ad(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(String(800))
    link: Mapped[str] # Link to project
    is_moderating: Mapped[bool] # Moderation status

    moderator_id: Mapped[int] = mapped_column(ForeignKey("moderators.id"), nullable=True)
    moderator: Mapped["Moderator"] = relationship(back_populates="in_moderating")

