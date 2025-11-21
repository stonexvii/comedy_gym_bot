from aiogram.filters.callback_data import CallbackData


class MyData(CallbackData, prefix='CMM'):
    button: str
