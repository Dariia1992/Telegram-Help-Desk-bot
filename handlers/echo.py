from aiogram import Router, types, F


router = Router()
tickets = {
    1: {
        "status": "Open",
        "priority": "High"
    },
    2: {
        "status": "Closed",
        "priority": "Low"
    },
    3: {
        "status": "In Progress",
        "priority": "High"
    }
}


def statistics(tickets):
    total = len(tickets)
    open_tickets = 0
    in_progress = 0
    closed = 0
    high_priority = 0

    for ticket in tickets.values():

        if ticket["status"] == "Open":
            open_tickets += 1

        elif ticket["status"] == "In Progress":
            in_progress += 1

        elif ticket["status"] == "Closed":
            closed += 1

        if ticket["priority"] == "High":
            high_priority += 1
    return (
        f"📊 HELP DESK STATISTICS\n\n"
        f"Total tickets: {total}\n"
        f"🟢 Open: {open_tickets}\n"
        f"🟡 In Progress: {in_progress}\n"
        f"🔴 Closed: {closed}\n"
        f"🔥 High priority: {high_priority}"
    )
    
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
    elif text == "📊 Statistics":
         result = statistics(tickets)
         await message.answer(result)
    
"""FSM!!"""






    

  