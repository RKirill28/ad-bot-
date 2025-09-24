from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db.schemas import ModeratorData


def kb_moders_list(moders_list: list[ModeratorData]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for moder in moders_list:
        builder.add()
