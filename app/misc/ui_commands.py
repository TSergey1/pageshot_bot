from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from app.misc.cmd import Button as btn
from app.misc.cmd import Command as cmd


async def set_ui_commands(bot: Bot):
    commands = [
        BotCommand(
            command=cmd.CHANGE_LANGUAGE,
            description=btn.CHANGE_LANGUAGE,
        ),
        BotCommand(
            command=cmd.CREATE_PAGESHOT,
            description=btn.CREATE_PAGESHOT,
        ),
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(),
    )
