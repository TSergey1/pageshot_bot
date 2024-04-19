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


# def back_kb(back: str) -> InlineKeyboardMarkup:
#     """Клавиатура возврата в предыдущее меню."""
#     back_btn = get_btn(btn.BACK_TXT, back)
#     return InlineKeyboardMarkup(inline_keyboard=[[back_btn]])


# def save_kb(back: str) -> InlineKeyboardMarkup:
#     """Клавиатура сохранения."""
#     save_btn = get_btn(btn.SAVE_TXT, cmd.AUTO_SAVE)
#     back_btn = get_btn(btn.BACK_TXT, back)
#     return InlineKeyboardMarkup(inline_keyboard=[[save_btn], [back_btn]])


# def main_kb() -> InlineKeyboardMarkup:
#     """Клавиатура главного меню."""
#     user_menu_btn = get_btn(btn.USER_MENU_TXT, cmd.USER)
#     auto_menu_btn = get_btn(btn.AUTO_MENU_TXT, cmd.AUTO_MENU)
#     search_btn = get_btn(btn.SEARCH_TXT, cmd.SEARCH)
#     return InlineKeyboardMarkup(
#         inline_keyboard=[[user_menu_btn, auto_menu_btn], [search_btn]]
#     )


# def confirm_del_kb(delete: str, back: str) -> InlineKeyboardMarkup:
#     """Клавиатура подтверждения удаления."""
#     delete_btn = get_btn(btn.DEL_CONFIRM_TXT, delete)
#     back_btn = get_btn(btn.BACK_TXT, back)
#     return InlineKeyboardMarkup(inline_keyboard=[[delete_btn], [back_btn]])


# def add_del_back_kb(add: str, delete: str, back: str) -> InlineKeyboardMarkup:
#     """Клавиатура добавления, удаления, возврата."""
#     add_btn = get_btn(btn.ADD_TXT, add)
#     delete_btn = get_btn(btn.DELETE_TXT, delete)
#     back_btn = get_btn(btn.BACK_TXT, back)
#     return InlineKeyboardMarkup(
#         inline_keyboard=[[add_btn, delete_btn], [back_btn]]
#     )
