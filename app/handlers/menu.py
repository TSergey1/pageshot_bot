import validators
from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

import app.keyboards.inline_keyboard as kb
from app.dao.user import UserDAO
from app.misc import msg
from app.misc.cmd import Command as cmd
from app.services.pageshot_service import (create_pageshot, get_info_for_foto,
                                           get_site_info)
from app.services.user_service import UserService

router = Router(name="main_menu-router")


@router.message(CommandStart())
@router.callback_query(F.data == cmd.RU)
@router.callback_query(F.data == cmd.EN)
async def cmd_start(call_or_message: CallbackQuery | Message) -> None:
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


@router.callback_query(F.data.startswith("language_"))
async def set_language(callback: CallbackQuery, user_dao: UserDAO) -> None:
    """Обработчик получение языка от пользователя."""
    lang: str = callback.data[9:]
    if await UserService.check_user(user_dao, callback.from_user.id):
        await UserService.update_user_lang(user_dao,
                                           callback.from_user.id,
                                           lang)
    else:
        await UserService.add_user(user_dao, callback.message.contact, lang)


@router.message()
async def get_pageshot(message: Message, bot: Bot) -> None:
    """Обработчик веденного url."""
    if validators.url(message.text):
        stub_message = await message.reply(_(msg.SEND_REQUEST))
        path_pageshot, time_processing = await create_pageshot(
            message.text,
            message.from_user.id,
            str(message.date)
        )
        await message.reply_photo(
            photo=FSInputFile(path_pageshot),
            caption=await get_info_for_foto(message.text, time_processing),
            reply_markup=kb.more_site()
        )
        await bot.delete_message(stub_message.chat.id, stub_message.message_id)
    else:
        await message.answer(_(msg.ERROR_URL))


@router.callback_query((F.data == __(cmd.MORE)))
async def more_site(callback: CallbackQuery) -> None:
    """Обработчик нажатия кнопки - Подробнее."""
    text = callback.message.reply_to_message.text
    await callback.answer(await get_site_info(text))
