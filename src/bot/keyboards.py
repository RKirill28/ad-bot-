from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db.schemas import ModeratorData


def show_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Показать меню")]], resize_keyboard=True
    )


def back_to_menu_btn() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back_to_menu")]
        ]
    )


def back_to_menu_with_delete_btn() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Назад", callback_data="back_to_menu_with_delete"
                )
            ]
        ]
    )


def admin_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Добавить модератора", callback_data="add_moder"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Удалить модератора", callback_data="delete_moder"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Список модераторов", callback_data="list_moders"
                )
            ],
        ]
    )


def moder_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Заявки", callback_data="requests")],
        ]
    )


def user_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Смотреть рекламу", callback_data="show_ads")],
            [InlineKeyboardButton(text="Разместить рекламу", callback_data="response")],
            [InlineKeyboardButton(text="Мои объявления", callback_data="my_responses")],
            [InlineKeyboardButton(text="О боте", callback_data="help")],
        ]
    )


def moders_list_menu(moders_list: list[ModeratorData]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    c = 0
    for moder in moders_list:
        builder.row(
            InlineKeyboardButton(
                text="", callback_data=f"remove_moder_{moder.telegram_id}"
            )
        )
