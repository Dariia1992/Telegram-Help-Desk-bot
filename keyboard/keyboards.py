from aiogram import types

button_1 = types.KeyboardButton(text="===== HELP DESK =====")

button_2 = types.KeyboardButton(text="Create")

button_3 = types.KeyboardButton(text="Exit")

keyboard_1 = [
    [button_1],
    [button_2, button_3]
]

kb_1 = types.ReplyKeyboardMarkup(keyboard=keyboard_1, resize_keyboard=True)

"""

┌──────────────────────────┐
│    /===== HELP DESK =====│
├──────────────┬───────────┤
│ /Create      │  /Exit    │    
└──────────────┴───────────┘

"""
