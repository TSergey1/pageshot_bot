from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.db.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def find_user_language(self, user_id: int) -> User | None:
        """Получить язык пользователя."""
        query = (
            select(User.language).where(User.tg_id == user_id,)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def set_user_lang(self, user_id: int, lang: str) -> None:
        """Обновить значение language для User."""
        query = (
            update(User).where(User.tg_id == user_id,).values(language=lang)
        )
        await self.session.execute(query)
        await self.session.commit()
