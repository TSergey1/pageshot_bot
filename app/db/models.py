from enum import Enum
from sqlalchemy import BigInteger, DateTime, String, func
# from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class LanguageEnum(Enum):
    RU = 'ru'
    EN = 'en'


class User(Base):
    __tablename__ = "app_user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    first_name: Mapped[str]
    language: Mapped[str] = mapped_column(String, default="ru")
    # language: Mapped[str] = mapped_column(PgEnum(LanguageEnum,
    #                                              name='language_enum',
    #                                              create_type=False),
    #                                        nullable=False,
    #                                         default=LanguageEnum.RU)
    data: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def __repr__(self):
        return f"tg_id={self.tg_id} name={self.language}"
