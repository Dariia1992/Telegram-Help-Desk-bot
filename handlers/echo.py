from aiogram import Router, types, F


router = Router()


#Если пользователь прислал текстовое сообщение — передай его функции echo()
@router.message(F.text)
async def echo(message: types.Message):
    # print(repr(message.text))
    text = message.text

    if text == "Create":
        await message.answer("Describe the problem: ")
                   
    elif text == "Exit":
        await message.answer("Good Bye")    
    
    elif text == "===== HELP DESK =====":
        await message.answer("""👋 Hello! Welcome to Help Desk.
    Here you can create a support request and describe your issue.""")   

    
"""FSM!!"""