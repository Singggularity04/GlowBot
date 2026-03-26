"""FAQ handler — question list and individual answers."""

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline import faq_list_kb, faq_back_kb
from texts.messages import FAQ_INTRO, FAQ_ANSWERS

router = Router()


@router.callback_query(F.data == "faq")
async def show_faq(callback: CallbackQuery) -> None:
    """Show FAQ question list."""
    await callback.answer()
    await callback.message.edit_text(FAQ_INTRO, reply_markup=faq_list_kb())


@router.callback_query(F.data.startswith("faq_"))
async def faq_answer(callback: CallbackQuery) -> None:
    """Show answer for a specific FAQ question."""
    faq_key = callback.data
    text = FAQ_ANSWERS.get(faq_key)
    if not text:
        await callback.answer("Вопрос не найден")
        return
    await callback.answer()
    await callback.message.edit_text(text, reply_markup=faq_back_kb())
