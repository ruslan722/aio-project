from aiogram import Dispatcher
from . import start, settings



async def include_routers(dp: Dispatcher):
    dp.include_routers(
        start.router,
        settings.router,
    )
