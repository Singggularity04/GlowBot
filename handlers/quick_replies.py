"""Quick replies — auto-responses to common client messages.

Registered LAST so it only catches messages not handled by FSM states.
Uses substring matching (case-insensitive) against known triggers.
"""

from aiogram import Router
from aiogram.types import Message

from keyboards.inline import main_menu_kb
from texts.messages import QUICK_REPLIES

router = Router()


@router.message()
async def handle_quick_reply(message: Message) -> None:
    """Check if message matches any known trigger phrase."""
    if not message.text:
        return

    text_lower = message.text.lower()

    for trigger, reply in QUICK_REPLIES.items():
        if trigger in text_lower:
            await message.answer(reply, reply_markup=main_menu_kb())
            return

    # Fallback — guide user to the menu
    await message.answer(
        "Я пока не понял запрос 🤔\n"
        "Попробуй выбрать нужный раздел из меню 👇",
        reply_markup=main_menu_kb(),
    )
