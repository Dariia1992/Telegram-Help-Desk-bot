from aiogram.fsm.state import State, StatesGroup

class TicketStates(StatesGroup):
    entering_title = State()
    entering_description = State()
    choosing_priority = State()
    entering_name = State()
    choosing_department = State()