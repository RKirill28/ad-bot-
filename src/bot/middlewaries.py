from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.exc import SQLAlchemyError

from db.session import session_maker


class DIMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        async with session_maker() as session:
            data["session"] = session

            try:
                result = await handler(event, data)
                return result
            except SQLAlchemyError as e:
                await session.rollback()  # в случае чего ролбэчим
                raise e
