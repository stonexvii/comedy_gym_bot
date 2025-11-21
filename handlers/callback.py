from aiogram import Router, Bot
from aiogram.types import CallbackQuery

from database import requests
from keyboards import ikb_start
from keyboards.callback_data import MyData
from utils import FileManager
from utils.enums import Path

callback_router = Router()


@callback_router.callback_query(MyData.filter())
async def callback_handler(callback: CallbackQuery, callback_data: MyData, bot: Bot):
    msg_text = await FileManager.read(Path.MESSAGES, callback_data.button)
    if callback_data.button == 'accept':
        await requests.register_user(callback.from_user.id)
    await bot.edit_message_text(
        chat_id=callback.from_user.id,
        message_id=callback.message.message_id,
        text=msg_text,
        disable_web_page_preview=True,
        reply_markup=ikb_start(url=callback_data.button == 'accept'),
    )
