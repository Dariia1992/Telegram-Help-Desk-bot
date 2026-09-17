from aiogram import types
from data.departments import departments
from data.priorities import priorities

button_create = types.KeyboardButton(text="Create ticket")
"""
Create ticket
user enter :
- user name
→ department
- phone
→ title
→ description
→ priority
(if priority == "High":
    emoji = "🔴"
elif priority == "Medium":
    emoji = "🟡"
else:
    emoji = "🟢")
→ save
Ticket created✅
"""
button_my = types.KeyboardButton(text="My tickets")
"""My tickets
→ find tiket
→ Show tiket
- del tick
-change priority
"""
button_stats = types.KeyboardButton(text="📊 Statistics")

button_exit = types.KeyboardButton(text="Exit")

keyboard_1 = [
    [button_create, button_my],
    [button_stats],
     [button_exit]
]

kb_1 = types.ReplyKeyboardMarkup(keyboard=keyboard_1, resize_keyboard=True)

# DEPARTMENTS
def get_departments_keyboard():
    keyboard = []

    for department in departments:

        button = types.InlineKeyboardButton(
            text=department,
            callback_data=f"department:{department}"
        )

        keyboard.append([button])

    return types.InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )
    
# PRIORITIES
def get_priorities_keyboard():
    keyboard = []

    for priority in priorities:

        button = types.InlineKeyboardButton(
            text=priority,
            callback_data=f"priority:{priority}"
        )

        keyboard.append([button])

    return types.InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )
    