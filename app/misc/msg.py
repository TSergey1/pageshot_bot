from aiogram.utils.markdown import hbold

# from app.misc.cmd import Button as btn

CHANGE_LANGUAGE = "Выберете язык"
SEND_REQUEST = "Запрос отправлен на сайт..."
ERROR_URL = "Введен не корректный url"



def start_msg(first_name: str) -> str:
    """Вернуть приветственное сообщение."""
    return (
        f"Привет {hbold(first_name)}! Меня зовут Pageshot_bot Я могу сделать "
        "скриншот любого сайта, который вы отправите мне в сообщении.\n"
        "Я работаю с протоколами http, https."
    )


# def autos_msg(autos: list[Auto] | None) -> str:
#     """Вернуть сообщение Мои автомобили."""
#     text = EMPTY_MSG
#     if autos:
#         text = "\n".join(map(str, autos))
#     return (
#         "* Мои автомобили *\n"
#         f"\n{btn.ADD_TXT} данные автомобиля в базу данных.\n"
#         f"\n{btn.DELETE_TXT} данные автомобиля из базы данных.\n"
#         "----------\n" + text
#     )
