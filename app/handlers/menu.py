import validators
from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

import app.keyboards.inline_keyboard as kb
from app.services.pageshot_service import create_pageshot
from app.misc import msg
from app.misc.cmd import Command as cmd


router = Router(name="main_menu-router")


@router.message(CommandStart())
@router.callback_query(F.data == cmd.RU)
@router.callback_query(F.data == cmd.EN)
async def cmd_start(call_or_message: CallbackQuery | Message,) -> None:
    """Обработчик главного меню бота."""
    text = _(msg.START_MASSAGE).format(
        first_name=call_or_message.from_user.first_name
    )
    if isinstance(call_or_message, Message):
        await call_or_message.answer(text, reply_markup=kb.main_kb())
    else:
        await call_or_message.message.edit_text(
                text, reply_markup=kb.main_kb()
            )


@router.callback_query(F.data == __(cmd.CHANGE_LANGUAGE))
async def change_language(callback: CallbackQuery) -> None:
    """Обработчик выбора языка."""
    await callback.message.edit_text(_(msg.CHANGE_LANGUAGE),
                                     reply_markup=kb.change_language())


@router.callback_query((F.data == __(cmd.RU)) | (F.data == __(cmd.EN)))
async def set_language(callback: CallbackQuery) -> None:
    """Обработчик получение языка от пользователя."""
    lang: str = callback.data[9:]
    # ________ запись языка в БД_____________
    await callback.message.edit_text(f"Вы выбрали {lang}")


@router.callback_query(F.data == __(cmd.CREATE_PAGESHOT))
async def enter_url(callback: CallbackQuery) -> None:
    """Обработчик кнопки - Добавить Image в чат."""
    bot_me = await callback.bot.me()
    await callback.answer(url=f"t.me/{bot_me.username}?start=1")


@router.message()
async def get_pageshot(message: Message, bot: Bot) -> None:
    """Обработчик веденного url."""
    if validators.url(message.text):
        await message.answer(_(msg.SEND_REQUEST))
        path_pageshot, time_processing, chat_id = await create_pageshot(
            message.text,
            message.chat.id, message.from_user.id,
            str(message.date)
        )
        await message.reply_photo(
            photo=FSInputFile(path_pageshot),
            caption=_(msg.SEND_PAGESHOT),
            reply_markup=kb.more_site()
        )
        await message.delete()
    else:
        await message.answer(_(msg.ERROR_URL))


@router.callback_query((F.data == __(cmd.MORE)))
async def more_site(callback: CallbackQuery) -> None:
    """Обработчик получение языка от пользователя."""
    await callback.answer("Крутой сайт!")
