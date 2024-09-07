import asyncio
import logging
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.i18n import I18n
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app import config
from app.handlers import menu
from app.middlewares.access import PrivateMiddleware
from app.middlewares.db_session import DbMiddleware
from app.middlewares.locales import BotI18nMiddleware
from app.misc.ui_commands import set_ui_commands

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG, format=config.LOG_FORMAT)
    logger.info("Bot start")

    redis = Redis(host=config.REDIS_HOST, port=config.REDIS_PORT)
    storage = RedisStorage(redis=redis)

    engine = create_async_engine(config.DB_URL, echo=config.DEBUG)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    dp = Dispatcher(storage=storage)

    i18n = I18n(path=Path(__file__).parent / 'locales',
                default_locale='ru',
                domain='message')
    BotI18nMiddleware(i18n).setup(dp)

    dp.update.middleware(DbMiddleware(sessionmaker))
    if config.GROUP:
        dp.update.middleware(PrivateMiddleware(config.GROUP))
    dp.update.middleware(BotI18nMiddleware(i18n))
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp.include_routers(menu.router)

    await set_ui_commands(bot)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stop")
