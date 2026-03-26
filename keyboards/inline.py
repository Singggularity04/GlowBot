"""All inline keyboards for the bot, built with InlineKeyboardBuilder."""

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def main_menu_kb() -> InlineKeyboardMarkup:
    """Main menu — 6 buttons in a 2-column layout."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🤖 Узнать о ботах", callback_data="about_bots")
    builder.button(text="💰 Тарифы", callback_data="tariffs")
    builder.button(text="⚙️ Как это работает", callback_data="how_it_works")
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="❓ Частые вопросы", callback_data="faq")
    builder.button(text="📬 Связаться со мной", callback_data="contact_me")
    builder.adjust(2, 2, 2)
    return builder.as_markup()


def back_to_menu_kb() -> InlineKeyboardMarkup:
    """Single 'Back to menu' button."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    return builder.as_markup()


def info_actions_kb() -> InlineKeyboardMarkup:
    """After 'About bots' — tariffs or application."""
    builder = InlineKeyboardBuilder()
    builder.button(text="💰 Посмотреть тарифы", callback_data="tariffs")
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(2, 1)
    return builder.as_markup()


def tariff_actions_kb() -> InlineKeyboardMarkup:
    """After tariffs display — pick tariff or apply."""
    builder = InlineKeyboardBuilder()
    builder.button(text="🎯 Подобрать тариф", callback_data="pick_tariff")
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(2, 1)
    return builder.as_markup()


def pick_tariff_kb() -> InlineKeyboardMarkup:
    """Tariff picker — 3 complexity levels."""
    builder = InlineKeyboardBuilder()
    builder.button(text="1️⃣ Одну-две задачи", callback_data="pick_1")
    builder.button(text="2️⃣ Несколько задач", callback_data="pick_2")
    builder.button(text="3️⃣ Много задач", callback_data="pick_3")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(1)
    return builder.as_markup()


def pick_result_kb() -> InlineKeyboardMarkup:
    """After tariff recommendation — apply or back."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="💰 Все тарифы", callback_data="tariffs")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(2, 1)
    return builder.as_markup()


def how_it_works_kb() -> InlineKeyboardMarkup:
    """After 'How it works' — apply or back."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(1)
    return builder.as_markup()


def faq_list_kb() -> InlineKeyboardMarkup:
    """FAQ question list — 6 questions + back."""
    builder = InlineKeyboardBuilder()
    builder.button(text="⏱ Сколько делается бот?", callback_data="faq_time")
    builder.button(text="👥 Для кого подходят?", callback_data="faq_who")
    builder.button(text="🎨 Под мой бизнес?", callback_data="faq_custom")
    builder.button(text="📋 Что нужно от меня?", callback_data="faq_need")
    builder.button(text="🔧 Можно изменить?", callback_data="faq_edit")
    builder.button(text="💡 Чем лучше переписок?", callback_data="faq_why_bot")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(1)
    return builder.as_markup()


def faq_back_kb() -> InlineKeyboardMarkup:
    """After FAQ answer — back to FAQ list or apply."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="❓ Другие вопросы", callback_data="faq")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(2, 1)
    return builder.as_markup()


def contact_kb() -> InlineKeyboardMarkup:
    """Contact section — apply or back."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📝 Оставить заявку", callback_data="start_application")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(1)
    return builder.as_markup()


# --- Application Form Keyboards ---

def niche_kb() -> InlineKeyboardMarkup:
    """Niche selection for application step 2."""
    builder = InlineKeyboardBuilder()
    builder.button(text="💅 Бьюти", callback_data="niche_Бьюти")
    builder.button(text="🔧 Услуги", callback_data="niche_Услуги")
    builder.button(text="📚 Онлайн-школа", callback_data="niche_Онлайн-школа")
    builder.button(text="🛍 Магазин", callback_data="niche_Магазин")
    builder.button(text="✏️ Другое", callback_data="niche_Другое")
    builder.adjust(2, 2, 1)
    return builder.as_markup()


def task_kb() -> InlineKeyboardMarkup:
    """Bot task selection for application step 3."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📥 Принимать заявки", callback_data="task_Принимать заявки")
    builder.button(text="📅 Записывать клиентов", callback_data="task_Записывать клиентов")
    builder.button(text="❓ Отвечать на вопросы", callback_data="task_Отвечать на вопросы")
    builder.button(text="💼 Продавать услуги", callback_data="task_Продавать услуги")
    builder.button(text="✏️ Другое", callback_data="task_Другое")
    builder.adjust(2, 2, 1)
    return builder.as_markup()


def tariff_select_kb() -> InlineKeyboardMarkup:
    """Tariff selection for application step 4."""
    builder = InlineKeyboardBuilder()
    builder.button(text="📦 Базовый", callback_data="app_tariff_Базовый")
    builder.button(text="⭐ Стандарт", callback_data="app_tariff_Стандарт")
    builder.button(text="🚀 PRO", callback_data="app_tariff_PRO")
    builder.button(text="🤔 Нужна помощь с выбором", callback_data="app_tariff_Нужна помощь с выбором")
    builder.adjust(3, 1)
    return builder.as_markup()


def cancel_application_kb() -> InlineKeyboardMarkup:
    """Cancel button shown during free-text application steps."""
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Отменить заявку", callback_data="cancel_application")
    return builder.as_markup()
