from datetime import date

from sqlalchemy import String, BigInteger, Date, Boolean
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(900), nullable=True)
    tg_username: Mapped[str] = mapped_column(String(900), nullable=True)
    register_date: Mapped[date] = mapped_column(Date)
    registered: Mapped[bool] = mapped_column(Boolean, default=False)
