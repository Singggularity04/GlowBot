"""Handler for /start command and main menu navigation."""

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.inline import main_menu_kb
from texts.messages import START_MESSAGE

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    """Greet user and show main menu. Clear any active FSM state."""
    await state.clear()
    await message.answer(START_MESSAGE, reply_markup=main_menu_kb())


@router.callback_query(F.data == "menu")
async def back_to_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """Return to main menu from any section."""
    await state.clear()
    await callback.answer()
    await callback.message.edit_text(START_MESSAGE, reply_markup=main_menu_kb())
