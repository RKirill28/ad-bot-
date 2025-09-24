from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import admin_menu, moder_menu, user_menu

import bot.services.message_service as message_service

router = Router()
admin = 1202267126
moders = [7375913205]


@router.message(CommandStart())
async def start(mess: Message) -> None:
    reply_markup = None
    text = ""
    if mess.from_user.id == admin:
        reply_markup = admin_menu()
        text = "Здравствуйте, господин. Ваше админ меню:"
    elif mess.from_user.id in moders:
        reply_markup = moder_menu()
        text = "Здравствуйте, дорогой модератор! Это ваше меню, удачной модерации:"
    else:
        reply_markup = user_menu()
        text = (
            "Здравствуйте, это бот для размещения и просмотра рекламных объявлений.\n"
        )
        "Здесь вы можете легко и просто разместить рекламу о своем проекте, и также можете найти интересующий вас проект!\n\n"
        "Это ваше меню, выберите один из пунктов:"

    await mess.answer(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(cb: CallbackQuery, session: AsyncSession) -> None:
    await cb.answer()
    text, reply_markup = await message_service.get_main_menu(session, cb.from_user.id)

    await cb.message.edit_text(text, reply_markup=reply_markup)
