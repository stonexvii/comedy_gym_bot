from aiogram import Router

from .callback import callback_router
from .command import command_router

main_router = Router()

main_router.include_routers(
    command_router,
    callback_router,
)
