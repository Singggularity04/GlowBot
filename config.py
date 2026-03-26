"""Bot configuration — loads secrets from .env file."""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
ADMIN_CHAT_ID: str = os.getenv("ADMIN_CHAT_ID", "")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in .env file")
if not ADMIN_CHAT_ID:
    raise ValueError("ADMIN_CHAT_ID is not set in .env file")
