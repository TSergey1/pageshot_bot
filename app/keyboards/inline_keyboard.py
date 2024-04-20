from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from app.misc.cmd import Button as btn
from app.misc.cmd import Command as cmd


def get_btn(text: str, action: str) -> InlineKeyboardButton:
    """Вернуть кнопку."""
    return InlineKeyboardButton(text=text, callback_data=action)


def main_kb() -> InlineKeyboardMarkup:
    """Клавиатура главного меню."""
    change_language_btn = get_btn(btn.CHANGE_LANGUAGE, cmd.CHANGE_LANGUAGE)
    create_pageshot = get_btn(btn.CREATE_PAGESHOT, cmd.CREATE_PAGESHOT)
    return InlineKeyboardMarkup(
        inline_keyboard=[[change_language_btn, create_pageshot], ]
    )


def change_language() -> InlineKeyboardMarkup:
    """Клавиатура выбора языка."""
    ru = get_btn(btn.RU, cmd.RU)
    en = get_btn(btn.EN, cmd.EN)
    return InlineKeyboardMarkup(
        inline_keyboard=[[ru, en], ]
    )


def more_site() -> InlineKeyboardMarkup:
    """Кнопка подробнее."""
    more = get_btn(btn.MORE, cmd.MORE)

    return InlineKeyboardMarkup(
        inline_keyboard=[[more,], ]
    )
