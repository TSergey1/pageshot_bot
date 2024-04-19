from aiogram import F, Router
from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
import validators

# from app.dao.user import UserDAO
import app.keyboards.inline_keyboard as kb
from app.services.pageshot import pageshot
from app.misc import msg
from app.misc.cmd import Command as cmd


router = Router(name="main_menu-router")


@router.message(CommandStart())
@router.callback_query(F.data == cmd.RU)
@router.callback_query(F.data == cmd.EN)
async def cmd_start(call_or_message: CallbackQuery | Message,) -> None:
    """Обработчик главного меню бота."""
    text = msg.start_msg(call_or_message.from_user.first_name)
    if isinstance(call_or_message, Message):
        await call_or_message.answer(text, reply_markup=kb.main_kb())
    else:
        await call_or_message.message.edit_text(
                text, reply_markup=kb.main_kb()
            )


@router.callback_query(F.data == cmd.CHANGE_LANGUAGE)
async def change_language(callback: CallbackQuery) -> None:
    """Обработчик выбора языка."""
    await callback.message.edit_text(msg.CHANGE_LANGUAGE,
                                     reply_markup=kb.change_language())


@router.callback_query((F.data == cmd.RU) | (F.data == cmd.EN))
async def set_language(callback: CallbackQuery) -> None:
    """Обработчик получение языка от пользователя."""
    lang: str = callback.data[9:]
    # ________ запись языка в БД_____________
    await callback.message.edit_text(f"Вы выбрали {lang}")


@router.message()
async def create_pageshot(message: Message, bot) -> None:
    """Обработчик веденного url."""
    if validators.url(message.text):
        await message.answer(msg.SEND_REQUEST)
        rez_shot = pageshot(message.text, message.chat.id, message.date)
        rez_shot = open('images/lsd.jpg', 'rb')
        await bot.send_photo(c.message.chat.id, Photo_lsd, caption='Я работаю')
    else:
        await message.answer(msg.ERROR_URL)





# @router.message(Command(cmd.MAIN))
# @router.callback_query(F.data == cmd.MAIN)
# async def cmd_menu(
#     call_or_message: CallbackQuery | Message,
#     state: FSMContext,
# ) -> None:
#     """Обработчик вызова главного меню."""
#     await state.clear()
#     if isinstance(call_or_message, Message):
#         await call_or_message.answer(msg.MAIN_MSG, reply_markup=main_kb())
#     else:
#         await call_or_message.message.edit_text(
#             msg.MAIN_MSG, reply_markup=main_kb()
#         )


# @router.message(Command(cmd.CANCEL))
# @router.message(F.text == btn.CANCEL_TXT)
# @router.callback_query(F.data == cmd.CANCEL)
# async def cmd_cancel(
#     call_or_message: CallbackQuery | Message,
#     state: FSMContext,
# ) -> None:
#     """Обработчик команды отмены."""
#     if await state.get_state():
#         await state.clear()
#         if isinstance(call_or_message, Message):
#             await call_or_message.answer(
#                 msg.CANCEL_MSG, reply_markup=ReplyKeyboardRemove()
#             )
#         else:
#             await call_or_message.message.edit_text(msg.CANCEL_MSG)
#     else:
#         await call_or_message.answer(
#             msg.STATE_CLEAR, reply_markup=ReplyKeyboardRemove()
#         )
