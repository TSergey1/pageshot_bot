from aiogram.types.base import Any, TelegramObject
from aiogram.utils.i18n.middleware import I18nMiddleware


class BotI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject,
                         data: dict[str, Any]) -> str:
        return "en"
