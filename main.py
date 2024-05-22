import asyncio
from aiogram import Bot, Dispatcher
from bot.handlers import include_routers
bot = Bot(token="7088407944:AAEj6aTi2xMD1BlCan6k8UTSP3cRKFhv2Eo")
dp = Dispatcher()

async def start():
     await include_routers(dp)
     await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
    