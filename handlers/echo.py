from aiogram import Router, types, F


router = Router()


# Если пользователь прислал текстовое сообщение — передай его функции echo()
@router.message(F.text)
async def echo(message: types.Message):
    text = message.text

    if text == "Create ticket":
        await message.answer("Describe the problem:")

    elif text == "My tickets":
        await message.answer("Your tickets:")

    elif text == "Exit":
        await message.answer("Good Bye")

    
"""FSM!!"""






    

  