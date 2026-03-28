"""Application (заявка) flow — 6-step FSM collecting client details."""

import logging

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline import (
    main_menu_kb,
    niche_kb,
    task_kb,
    tariff_select_kb,
    cancel_application_kb,
)
from texts.messages import (
    APP_STEP_NAME,
    APP_STEP_NICHE,
    APP_STEP_NICHE_CUSTOM,
    APP_STEP_TASK,
    APP_STEP_TARIFF,
    APP_STEP_DESCRIPTION,
    APP_STEP_CONTACT,
    APP_CONFIRMATION,
    ADMIN_NOTIFICATION,
    START_MESSAGE,
)
from config import ADMIN_CHAT_ID

logger = logging.getLogger(__name__)

router = Router()


class ApplicationForm(StatesGroup):
    """FSM states for the application flow."""
    name = State()
    niche = State()
    niche_custom = State()  # free-text input when user picks "Другое"
    bot_task = State()
    tariff = State()
    description = State()
    contact = State()


# --- Entry point ---

@router.callback_query(F.data == "start_application")
async def start_application(callback: CallbackQuery, state: FSMContext) -> None:
    """Begin the application flow — ask for name."""
    await state.set_state(ApplicationForm.name)
    await callback.answer()
    await callback.message.edit_text(
        APP_STEP_NAME, reply_markup=cancel_application_kb()
    )


# --- Cancel ---

@router.callback_query(F.data == "cancel_application")
async def cancel_application(callback: CallbackQuery, state: FSMContext) -> None:
    """Cancel the application at any step."""
    await state.clear()
    await callback.answer("Заявка отменена")
    await callback.message.edit_text(START_MESSAGE, reply_markup=main_menu_kb())


# --- Step 1: Name (free text) ---

@router.message(ApplicationForm.name)
async def process_name(message: Message, state: FSMContext) -> None:
    """Save name, ask for niche."""
    await state.update_data(name=message.text)
    await state.set_state(ApplicationForm.niche)
    await message.answer(
        APP_STEP_NICHE.format(name=message.text),
        reply_markup=niche_kb(),
    )


# --- Step 2: Niche (inline buttons) ---

@router.callback_query(ApplicationForm.niche, F.data.startswith("niche_"))
async def process_niche(callback: CallbackQuery, state: FSMContext) -> None:
    """Save niche selection or ask for custom input if 'Другое'."""
    niche = callback.data.replace("niche_", "")
    await callback.answer()

    if niche == "Другое":
        # Ask user to type their niche manually
        await state.set_state(ApplicationForm.niche_custom)
        await callback.message.edit_text(
            APP_STEP_NICHE_CUSTOM, reply_markup=cancel_application_kb()
        )
        return

    await state.update_data(niche=niche)
    await state.set_state(ApplicationForm.bot_task)
    await callback.message.edit_text(APP_STEP_TASK, reply_markup=task_kb())


@router.message(ApplicationForm.niche_custom)
async def process_niche_custom(message: Message, state: FSMContext) -> None:
    """Save free-text niche, go straight to contact — tariff already chosen."""
    await state.update_data(niche=message.text)
    await state.set_state(ApplicationForm.contact)
    await message.answer(
        APP_STEP_CONTACT, reply_markup=cancel_application_kb()
    )


# --- Step 3: Bot task (inline buttons) ---

@router.callback_query(ApplicationForm.bot_task, F.data.startswith("task_"))
async def process_task(callback: CallbackQuery, state: FSMContext) -> None:
    """Save task selection, ask for preferred tariff."""
    task = callback.data.replace("task_", "")
    await state.update_data(bot_task=task)
    await state.set_state(ApplicationForm.tariff)
    await callback.answer()
    await callback.message.edit_text(APP_STEP_TARIFF, reply_markup=tariff_select_kb())


# --- Step 4: Tariff (inline buttons) ---

@router.callback_query(ApplicationForm.tariff, F.data.startswith("app_tariff_"))
async def process_tariff(callback: CallbackQuery, state: FSMContext) -> None:
    """Save tariff choice, ask for free-text description."""
    tariff = callback.data.replace("app_tariff_", "")
    await state.update_data(tariff=tariff)
    await state.set_state(ApplicationForm.description)
    await callback.answer()
    await callback.message.edit_text(
        APP_STEP_DESCRIPTION, reply_markup=cancel_application_kb()
    )


# --- Step 5: Description (free text) ---

@router.message(ApplicationForm.description)
async def process_description(message: Message, state: FSMContext) -> None:
    """Save description, ask for contact."""
    await state.update_data(description=message.text)
    await state.set_state(ApplicationForm.contact)
    await message.answer(
        APP_STEP_CONTACT, reply_markup=cancel_application_kb()
    )


# --- Step 6: Contact (free text) ---

@router.message(ApplicationForm.contact)
async def process_contact(message: Message, state: FSMContext, bot: Bot) -> None:
    """Save contact, finalize application, notify admin."""
    await state.update_data(contact=message.text)
    data = await state.get_data()
    await state.clear()

    # Confirm to the client
    await message.answer(APP_CONFIRMATION, reply_markup=main_menu_kb())

    # Notify admin with structured application data
    admin_text = ADMIN_NOTIFICATION.format(
        name=data.get("name", "—"),
        niche=data.get("niche", "—"),
        task=data.get("bot_task", "—"),
        tariff=data.get("tariff", "—"),
        description=data.get("description", "—"),
        contact=data.get("contact", "—"),
        user_id=message.from_user.id,
    )

    try:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_text)
    except Exception as exc:
        logger.error("Failed to send admin notification: %s", exc)
