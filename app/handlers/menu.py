from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
import validators

# from app.dao.user import UserDAO
import app.keyboards.inline_keyboard as kb
from app.misc import msg
from app.misc.cmd import Button as btn
from app.misc.cmd import Command as cmd


router = Router(name="main_menu-router")

@router.message(CommandStart())
@router.callback_query(F.data == cmd.RU)
@router.callback_query(F.data == cmd.EN)
async def cmd_start(call_or_message: CallbackQuery | Message,) -> None:
    """Обработчик запуска бота."""
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
    await callback.message.delete()
    await callback.message.answer(msg.CHANGE_LANGUAGE,
                                  reply_markup=kb.change_language())


@router.callback_query((F.data == cmd.RU) | (F.data == cmd.EN))
async def set_language(callback: CallbackQuery) -> None:
    """Обработчик получение языка от пользователя."""
    await callback.message.delete()
    lang: str = callback.data[9:]
    #####
    await callback.message.answer(f"Вы выбрали {lang}")


@router.message()
async def pageshot(message: Message) -> None:
    """Обработчик веденного url."""
    if validators.url(message):
        await message.answer(msg.SEND_REQUEST)
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
