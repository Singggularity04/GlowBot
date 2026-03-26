"""Handlers for tariffs display and tariff picker quiz."""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import tariff_actions_kb, pick_tariff_kb, pick_result_kb
from texts.messages import TARIFFS, PICK_TARIFF_Q1, PICK_TARIFF_RESULTS

router = Router()


@router.callback_query(F.data == "tariffs")
async def show_tariffs(callback: CallbackQuery) -> None:
    """Display all 3 tariff plans."""
    await callback.answer()
    await callback.message.edit_text(TARIFFS, reply_markup=tariff_actions_kb())


@router.callback_query(F.data == "pick_tariff")
async def start_tariff_picker(callback: CallbackQuery) -> None:
    """Start the tariff recommendation quiz."""
    await callback.answer()
    await callback.message.edit_text(PICK_TARIFF_Q1, reply_markup=pick_tariff_kb())


@router.callback_query(F.data.startswith("pick_"))
async def tariff_recommendation(callback: CallbackQuery) -> None:
    """Show tariff recommendation based on user's answer."""
    pick_key = callback.data  # pick_1, pick_2, pick_3
    text = PICK_TARIFF_RESULTS.get(pick_key, PICK_TARIFF_RESULTS["pick_2"])
    await callback.answer()
    await callback.message.edit_text(text, reply_markup=pick_result_kb())
