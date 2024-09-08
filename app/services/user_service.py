from aiogram.types.user import User as telegram_user

from app.dao.user import UserDAO
from app.db.models import User


class UserService:
    """Сервис для работы с пользователями."""

    @classmethod
    async def check_user(cls, dao: UserDAO, tg_id: int) -> bool:
        """Проверить наличие пользователя в базе."""
        if await dao.find_one_or_none(tg_id=tg_id):
            return True
        return False

    @classmethod
    async def add_user(cls,
                       dao: UserDAO,
                       user: telegram_user,
                       lang: str) -> None:
        """Добавить пользователя в базу."""
        await dao.add(
            tg_id=user.id,
            first_name=user.first_name,
            language=lang
        )

    @classmethod
    async def get_user_lang(cls, dao: UserDAO, tg_id: int) -> User | None:
        """Вернуть язык пользователя."""
        return await dao.find_user_language(tg_id=tg_id)

    @classmethod
    async def update_user_lang(
        cls, dao: UserDAO,
        user_id: int,
        lang: str
    ) -> None:
        """Изменить язык пользователя."""
        await dao.set_user_lang(user_id=user_id, lang=lang)
