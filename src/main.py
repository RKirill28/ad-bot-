import asyncio
import datetime
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from bot.middlewaries import DIMiddleware
from config import settings

from bot.main import router as main_router
from bot.admin_router import router as admin_router
from bot.moder_router import router as moder_router
from bot.user_router import router as user_router



async def main():
    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(
        token=settings.bot_config.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=True)

    main_router.include_routers(admin_router, moder_router, user_router)
    main_router.message.outer_middleware(DIMiddleware())
    main_router.callback_query.outer_middleware(DIMiddleware())
    dp.include_router(main_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logger_format = "%(levelname)s:%(name)s:%(funcName)s() - %(message)s"
    logging.basicConfig(level=logging.INFO, format=logger_format)

    logger = logging.getLogger()
    foramtter = logging.Formatter(logger_format)

    # file_handler = logging.FileHandler(
    #     f"./logs/{datetime.datetime.now().strftime('%Y:%m:%d - %H:%M:%S')}_bot.log",
    #     encoding="utf-8",
    #     mode="a",
    # )
    # file_handler.setFormatter(foramtter)
    # file_handler.setLevel(logging.DEBUG)

    asyncio.run(main())
