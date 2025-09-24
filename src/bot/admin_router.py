from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

import bot.keyboards as keyboards
import bot.services.moderator as moderator_serivce

import bot.services.message_service as message_service

router = Router()
moders = []


@router.callback_query(F.data == "list_moders")
async def show_moder_list(cb: CallbackQuery, session: AsyncSession) -> None:
    # use some service for get moder list and format for tg message
    await cb.answer()
    data = await moderator_serivce.get_moderators_list(session)
    text = message_service.get_moders_list_text(data)

    await cb.message.edit_text(text, reply_markup=keyboards.back_to_menu_btn())
