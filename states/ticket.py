from aiogram.fsm.state import State, StatesGroup


class TicketStates(StatesGroup):
    choosing_department = State()
    entering_name = State()
    entering_phone = State()
    entering_title = State()
    entering_description = State()
    choosing_priority = State()
    