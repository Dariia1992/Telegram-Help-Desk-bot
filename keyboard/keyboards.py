from aiogram import types

button_create = types.KeyboardButton(text="Create ticket")
"""Create ticket
      ↓
1. Ждём название проблемы
      ↓
2. Ждём описание
      ↓
3. Ждём приоритет
      ↓
Ticket created✅

Create ticket
→ title
→ description
→ priority
→ save
"""
button_my = types.KeyboardButton(text="My tickets")
"""My tickets
→ find tiket
→ Show tiket"""


button_exit = types.KeyboardButton(text="Exit")

keyboard_1 = [
    [button_create, button_my],
    [button_exit]
]

kb_1 = types.ReplyKeyboardMarkup(keyboard=keyboard_1, resize_keyboard=True)

"""

┌──────────────────────────┐
│    /===== HELP DESK =====│
├──────────────┬───────────┤
│ /Create      │  /Exit    │    
└──────────────┴───────────┘







"""
