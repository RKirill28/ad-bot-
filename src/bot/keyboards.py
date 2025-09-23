from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def show_menu() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Показать меню")]], resize_keyboard=True
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
