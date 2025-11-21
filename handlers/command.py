from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from database import User
from keyboards import ikb_start
from middlewares import UserMiddleware
from utils import FileManager
from utils.enums import Path

command_router = Router()
command_router.message.middleware(UserMiddleware())


@command_router.message(Command('start'))
async def command_start(message: Message, user: User):
    if user and user.registered:
        msg_text = await FileManager.read(Path.REGISTERED, name=message.from_user.full_name)
        keyboard = None
    else:
        msg_text = await FileManager.read(Path.START_COMMAND, name=message.from_user.full_name)
        keyboard = ikb_start(about=True)
    await message.answer(
        text=msg_text,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
