from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.base import BaseDAO
from app.db.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def find_user_language(self, language) -> User | None:
        """Получить язык пользователя."""
        query = (
            select(User).values(language=language)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def set_user_banned_true(self, **data) -> None:
        """Обновить значение поля banned на True."""
        query = update(User).filter_by(**data).values(banned=True)
        await self.session.execute(query)
        await self.session.commit()
