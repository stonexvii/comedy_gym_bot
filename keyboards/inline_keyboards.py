from aiogram.utils.keyboard import InlineKeyboardBuilder

from .buttons import KeyboardButton
from .callback_data import MyData


def ikb_start(about: bool = False, url: bool = False):
    keyboard = InlineKeyboardBuilder()
    if url:
        keyboard.button(**KeyboardButton('Заполнить анкету', url='https://forms.gle/7jgYjvRoL1a9mhsX8').as_kwargs())
    else:
        keyboard.button(**KeyboardButton('Хочу записаться!', MyData, button='accept').as_kwargs())
        if about:
            keyboard.button(**KeyboardButton('Давай, подробнее...', MyData, button='about').as_kwargs())
    keyboard.adjust(1)
    return keyboard.as_markup()
