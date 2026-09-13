from aiogram import Router, types
from aiogram.filters.command import Command

from keyboard.keyboards import kb_1

router = Router()

# Когда пользователь пишет /start,
# декоратор вызывает функцию command_start()
@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer("Hello",reply_markup=kb_1)


# Когда пользователь пишет /stop,
# декоратор вызывает функцию command_stop()
@router.message(Command("stop"))
async def command_stop(message: types.Message):
    await message.answer("Good Bye")
