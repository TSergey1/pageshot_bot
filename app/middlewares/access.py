from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class PrivateMiddleware(BaseMiddleware):
    def __init__(self, group: str):
        self.group = group

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        tg_id = data["event_from_user"].id
        status = ["creator", "administrator", "member"]
        member = await event.bot.get_chat_member(self.group, tg_id)

        if (member.status in status):
            return await handler(event, data)
