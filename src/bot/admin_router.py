from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

import bot.keyboards as keyboards
import bot.services.moderator as moderator_serivce
import bot.services.admin_service as admin_service

from bot.state import AdminStates
from bot.keyboards import back_to_menu_btn

import bot.services.message_service as message_service

router = Router()


async def send_main_menu(mess: Message, session: AsyncSession) -> None:
    text, reply_markup = await message_service.get_main_menu(session, mess.from_user.id)

    await mess.answer(text, reply_markup=reply_markup)


@router.callback_query(F.data == "list_moders")
async def show_moder_list(cb: CallbackQuery, session: AsyncSession) -> None:
    # use some service for get moder list and format for tg message
    await cb.answer()
    data = await moderator_serivce.get_moderators_list(session)
    text = message_service.get_moders_list_text(data)

    await cb.message.edit_text(text, reply_markup=keyboards.back_to_menu_btn())


@router.callback_query(F.data == "add_moder")
async def add_moder(cb: CallbackQuery, state: FSMContext) -> None:
    await cb.answer()

    await state.set_state(AdminStates.add_new_moder)  # устанавливаю состояние

    await cb.message.answer(
        "Отправьте ID пользователя Telegram, которого хотите добавить как модератора:",
        reply_markup=back_to_menu_btn(),
    )


@router.callback_query(F.data == "delete_moder")
async def delete_moder(
    cb: CallbackQuery, state: FSMContext, session: AsyncSession
) -> None:
    await cb.answer()

    data = await moderator_serivce.get_moderators_list(session)
    text = message_service.get_moders_list_text(data)

    await cb.message.edit_text(text, reply_markup=keyboards.back_to_menu_btn())
    await cb.message.answer("Напишите ID модератора, которого хотите удалить:")

    await state.set_state(AdminStates.delete_moder)


@router.message(AdminStates.delete_moder)
async def delete_moder(
    mess: Message, bot: Bot, state: FSMContext, session: AsyncSession
) -> None:
    text = mess.text.strip()

    if not text.isdigit():
        await mess.answer(
            "Это не число, попробуйте еще раз:", reply_markup=back_to_menu_btn()
        )

    try:
        user_info = await bot.get_chat(int(text))
        try:
            await admin_service.delete_moder(session, int(text))
        except IntegrityError:
            await mess.answer(
                "Такого модера не сущетсвует, попробуйте еще раз:",
                reply_markup=back_to_menu_btn(),
            )
            return

        await mess.answer(
            f"Удалил модера @{user_info.username} | {user_info.first_name} | {user_info.last_name}"
        )

        await state.clear()  # WARN: Чистим состояние, полностью

        await send_main_menu(mess, session)
    except TelegramBadRequest:
        await mess.answer(
            "Не удалось найти такого пользователя, попробуйте еще раз:",
            reply_markup=back_to_menu_btn(),
        )


@router.message(AdminStates.add_new_moder)
async def get_user_id_for_add_moder(
    mess: Message, bot: Bot, state: FSMContext, session: AsyncSession
) -> None:
    text = mess.text.strip()

    if not text.isdigit():
        await mess.answer(
            "Это не число, попробуйте еще раз:", reply_markup=back_to_menu_btn()
        )

    try:
        user_info = await bot.get_chat(int(text))
        try:
            await admin_service.add_moder(session, user_info)
        except IntegrityError:
            await mess.answer(
                "Такой юзер уже существует, попробуйте еще раз:",
                reply_markup=back_to_menu_btn(),
            )
            return

        await mess.answer(
            f"Добавил юзера @{user_info.username} | {user_info.first_name} | {user_info.last_name}"
        )

        await state.clear()  # WARN: Чистим состояние, полностью

        await send_main_menu(mess, session)
    except TelegramBadRequest:
        await mess.answer(
            "Не удалось найти такого пользователя, попробуйте еще раз:",
            reply_markup=back_to_menu_btn(),
        )
