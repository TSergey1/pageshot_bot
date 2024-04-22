import validators
import whois

from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from app.dao.user import UserDAO
import app.keyboards.inline_keyboard as kb
from app.misc import msg
from app.misc.cmd import Command as cmd
from app.services.pageshot_service import create_pageshot, get_site_info
from app.services.user_service import UserService

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
async def set_language(callback: CallbackQuery, user_dao: UserDAO) -> None:
    """Обработчик получение языка от пользователя."""
    lang: str = callback.data[9:]
    if await UserService.check_user(user_dao, callback.from_user.id):
        await UserService.update_user_lang(callback.from_user.id, lang)
    else:
        await UserService.add_user(user_dao, callback.message.contact, lang)


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
        path_pageshot, time_processing = await create_pageshot(
            message.text,
            message.from_user.id,
            str(message.date)
        )
        site_info = whois.whois(message.text)
        await message.reply_photo(
            photo=FSInputFile(path_pageshot),
            caption=f"{site_info.domain_name}\n"
                    f"{message.text}\n"
                    f"{time_processing} ",
            reply_markup=kb.more_site()
        )
        await message.delete()
    else:
        await message.answer(_(msg.ERROR_URL))


@router.callback_query((F.data == __(cmd.MORE)))
async def more_site(callback: CallbackQuery) -> None:
    """Обработчик нажатия кнопки -Подробнее."""
    await callback.answer(get_site_info(callback.message.text))
