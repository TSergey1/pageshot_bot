import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types.base import Any, TelegramObject
from aiogram.utils.i18n import I18n, ConstI18nMiddleware
from aiogram.utils.i18n.middleware import I18nMiddleware
from redis.asyncio import Redis
# from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app import config
from app.handlers import menu
# from app.middlewares.access import PrivateMiddleware
# from app.middlewares.db_session import DbMiddleware
# from app.misc.ui_commands import set_ui_commands

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG, format=config.LOG_FORMAT)
    logger.info("Bot start")

    redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    storage = RedisStorage(redis=redis)

    # engine = create_async_engine(config.DB_URL, echo=config.DEBUG)
    # sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    i18n = I18n(path=Path(__file__).parent / 'locales',
                default_locale='ru',
                domain='message')
    # i18n_middleware = ConstI18nMiddleware(i18n=i18n, locale="ru")

    class BotI18nMiddleware(I18nMiddleware):
        async def get_locale(self, event: TelegramObject, data: dict[str, Any]) -> str:
            return 'ru'

    dp = Dispatcher(storage=storage)
    BotI18nMiddleware(i18n).setup(dp)
    # dp = Dispatcher()
    # dp.update.middleware(DbMiddleware(sessionmaker))
    # dp.update.middleware(PrivateMiddleware(config.GROUP))
    dp.include_routers(menu.router)
    dp.update.outer_middleware(BotI18nMiddleware(i18n))
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

    # await set_ui_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")
