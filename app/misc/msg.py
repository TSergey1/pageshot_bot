from aiogram.utils.markdown import hbold


CHANGE_LANGUAGE = "Выберете язык:"
SEND_REQUEST = "Обработка ..."
ERROR_URL = "Введен не корректный url"

SEND_PAGESHOT = "Вот ваш скрин!!!"


def start_msg(first_name: str) -> str:
    """Вернуть приветственное сообщение."""
    return (
        f"Привет {hbold(first_name)}! Меня зовут Pageshot_bot Я могу сделать "
        "скриншот любого сайта, который вы отправите мне в сообщении.\n"
        "Я работаю с протоколами http, https."
    )
