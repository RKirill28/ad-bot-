from aiogram import F, Bot, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.keyboards import admin_menu, moder_menu, user_menu

import bot.services.message_service as message_service

router = Router()
admin = 1202267126
moders = [7375913205]


@router.message(CommandStart())
async def start(mess: Message, session: AsyncSession) -> None:
    text, reply_markup = await message_service.get_main_menu(session, mess.from_user.id)

    await mess.answer(text=text, reply_markup=reply_markup)


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(cb: CallbackQuery, session: AsyncSession) -> None:
    await cb.answer()
    text, reply_markup = await message_service.get_main_menu(session, cb.from_user.id)

    await cb.message.edit_text(text, reply_markup=reply_markup)


@router.callback_query(F.data == "back_to_menu_with_delete")
async def back_to_menu(
    cb: CallbackQuery, state: FSMContext, session: AsyncSession
) -> None:
    await cb.message.delete()
    await state.clear()
