"""GlowBot — Telegram bot for business automation leads.

Entry point: creates Bot + Dispatcher, registers all routers, starts polling.
"""

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN

# Import routers — order matters: specific handlers first, fallback last
from handlers import start, info, tariffs, faq, application, quick_replies


def _build_dispatcher() -> Dispatcher:
    """Register all routers in correct priority order."""
    dp = Dispatcher()
    dp.include_router(start.router)         # /start + menu
    dp.include_router(info.router)          # about, how it works, contact
    dp.include_router(tariffs.router)       # tariffs + picker
    dp.include_router(faq.router)           # FAQ
    dp.include_router(application.router)   # FSM application flow
    dp.include_router(quick_replies.router) # fallback — must be last
    return dp


async def main() -> None:
    """Initialize bot and start long-polling."""
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = _build_dispatcher()

    logging.info("GlowBot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stdout,
    )
    asyncio.run(main())
