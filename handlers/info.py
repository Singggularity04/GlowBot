"""Handlers for 'About bots', 'How it works', and 'Contact me' sections."""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import info_actions_kb, how_it_works_kb, contact_kb
from texts.messages import ABOUT_BOTS, HOW_IT_WORKS, CONTACT_ME

router = Router()


@router.callback_query(F.data == "about_bots")
async def about_bots(callback: CallbackQuery) -> None:
    """Show information about what bots can do for business."""
    await callback.answer()
    await callback.message.edit_text(ABOUT_BOTS, reply_markup=info_actions_kb())


@router.callback_query(F.data == "how_it_works")
async def how_it_works(callback: CallbackQuery) -> None:
    """Explain the 5-step process of getting a bot."""
    await callback.answer()
    await callback.message.edit_text(HOW_IT_WORKS, reply_markup=how_it_works_kb())


@router.callback_query(F.data == "contact_me")
async def contact_me(callback: CallbackQuery) -> None:
    """Show direct contact information."""
    await callback.answer()
    await callback.message.edit_text(CONTACT_ME, reply_markup=contact_kb())
