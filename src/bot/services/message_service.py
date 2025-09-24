from sqlalchemy.ext.asyncio import AsyncSession
from db.repositories.moderator_repo import ModeratorRepo
from db.schemas import ModeratorData
from config import settings

import bot.keyboards as keyboards


def get_moders_list_text(moders_list: list[ModeratorData]) -> str:
    text = "Список модераторов:\n"
    for moder in moders_list:
        text += f"{moder.telegram_id}(@{moder.username}) - {moder.first_name}\n"
    return text


async def get_main_menu(session: AsyncSession, user_id: int):
    reply_markup = None
    text = ""

    moders_ids = await ModeratorRepo.get_ids(session)

    if user_id == int(settings.bot_config.admin_id):
        reply_markup = keyboards.admin_menu()
        text = "Здравствуйте, господин. Ваше админ меню:"
    elif user_id in moders_ids:
        reply_markup = keyboards.moder_menu()
        text = "Здравствуйте, дорогой модератор! Это ваше меню, удачной модерации:"
    else:
        reply_markup = keyboards.user_menu()
        text = (
            "Здравствуйте, это бот для размещения и просмотра рекламных объявлений.\n"
        )
        "Здесь вы можете легко и просто разместить рекламу о своем проекте, и также можете найти интересующий вас проект!\n\n"
        "Это ваше меню, выберите один из пунктов:"
    return text, reply_markup
