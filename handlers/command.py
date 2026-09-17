from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from keyboard.keyboards import (
    kb_1,
    get_departments_keyboard,
    get_priorities_keyboard
)
from states.ticket import TicketStates


router = Router()


# START
@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(
        "👋 Hello! Welcome to Help Desk.\n"
        "Here you can create a support request and describe your issue.",
        reply_markup=kb_1
    )


# STOP
@router.message(Command("stop"))
async def command_stop(message: types.Message):
    await message.answer("👋 Good Bye")


# CREATE TICKET
@router.message(F.text == "Create ticket")
async def ticket_start(
    message: types.Message,
    state: FSMContext
):
    await state.set_state(TicketStates.choosing_department)

    await message.answer("🎫 Creating a ticket")

    await message.answer(
        "🏢 Choose department:",
        reply_markup=get_departments_keyboard()
    )


# CHOOSE DEPARTMENT
@router.callback_query(
    TicketStates.choosing_department,
    F.data.startswith("department:")
)
async def choose_department(
    callback: types.CallbackQuery,
    state: FSMContext
):
    department = callback.data.split(":", 1)[1]

    await state.update_data(department=department)

    await callback.message.answer(
        f"✅ You selected department: {department}"
    )

    await state.set_state(TicketStates.entering_name)

    await callback.message.answer("👤 Enter your name:")

    await callback.answer()


# ENTER NAME
@router.message(TicketStates.entering_name)
async def enter_name(
    message: types.Message,
    state: FSMContext
):
    name = message.text

    await state.update_data(name=name)

    await state.set_state(TicketStates.entering_phone)

    await message.answer("📱 Enter your phone:")


# ENTER PHONE
@router.message(TicketStates.entering_phone)
async def enter_phone(
    message: types.Message,
    state: FSMContext
):
    phone = message.text

    await state.update_data(phone=phone)

    await state.set_state(TicketStates.entering_title)

    await message.answer("📝 Enter ticket title:")


# ENTER TITLE
@router.message(TicketStates.entering_title)
async def enter_title(
    message: types.Message,
    state: FSMContext
):
    title = message.text

    await state.update_data(title=title)

    await state.set_state(TicketStates.entering_description)

    await message.answer("💬 Describe your problem:")


# ENTER DESCRIPTION
@router.message(TicketStates.entering_description)
async def enter_description(
    message: types.Message,
    state: FSMContext
):
    description = message.text

    await state.update_data(description=description)

    await state.set_state(TicketStates.choosing_priority)

    await message.answer(
        "⚡ Choose priority:",
        reply_markup=get_priorities_keyboard()
    )


# CHOOSE PRIORITY
@router.callback_query(
    TicketStates.choosing_priority,
    F.data.startswith("priority:")
)
async def choose_priority(
    callback: types.CallbackQuery,
    state: FSMContext
):
    priority = callback.data.split(":", 1)[1]

    await state.update_data(priority=priority)

    data = await state.get_data()

    if priority == "High":
        emoji = "🔴"
    elif priority == "Medium":
        emoji = "🟡"
    else:
        emoji = "🟢"

    await callback.message.answer(
        f"✅ Ticket created!\n\n"
        f"👤 Name: {data['name']}\n"
        f"📱 Phone: {data['phone']}\n"
        f"🏢 Department: {data['department']}\n"
        f"📝 Title: {data['title']}\n"
        f"💬 Description: {data['description']}\n"
        f"{emoji} Priority: {data['priority']}"
    )

    await state.clear()

    await callback.message.answer(
        "🏠 Back to main menu:",
        reply_markup=kb_1
    )

    await callback.answer()