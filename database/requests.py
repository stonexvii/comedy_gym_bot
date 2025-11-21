from datetime import date

from aiogram.types import Message
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .db_engine import async_session, engine
from .tables import Base, User


def connection(function):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            try:
                return await function(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    return wrapper


async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)


@connection
async def get_user(message: Message, session: AsyncSession):
    user = await session.scalar(select(User).where(User.tg_id == message.from_user.id))
    if not user:
        user = User(
            tg_id=message.from_user.id,
            name=message.from_user.full_name,
            tg_username=message.from_user.username,
            register_date=date.today(),
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user


@connection
async def register_user(user_tg_id: int, session: AsyncSession) -> User:
    stmt = update(User).where(User.tg_id == user_tg_id).values(registered=True)
    await session.execute(stmt)
    await session.commit()
