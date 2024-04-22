from aiogram.types.base import Any, TelegramObject
from aiogram.utils.i18n.middleware import I18nMiddleware


class BotI18nMiddleware(I18nMiddleware):
    # async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
    #     """
    #     Detect current user locale based on event and context.

    #     **This method must be defined in child classes**

    #     :param event:
    #     :param data:
    #     :return:
    #     """

    #     event.from_user.id
    #     pass
    async def get_locale(self, event: TelegramObject,
                         data: dict[str, Any]) -> str:
        return 'ru'






# class DbMiddleware(BaseMiddleware):
#     def __init__(
#         self,
#         session_pool: async_sessionmaker,
#     ):
#         super().__init__()
#         self.session_pool = session_pool

#     async def __call__(
#         self,
#         handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: Dict[str, Any],
#     ) -> Any:
#         async with self.session_pool() as session:
#             data["user_dao"] = UserDAO(session)
#             return await handler(event, data)