from aiogram import Bot, Dispatcher
import asyncio


from handlers import command, echo

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN_TG  = os.getenv("TOKEN_TG")


bot = Bot(token=TOKEN_TG)

dp = Dispatcher()

dp.include_router(command.router)
dp.include_router(echo.router)


async def main():
    print("BOT STARTED")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    
    
