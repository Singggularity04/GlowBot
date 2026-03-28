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


def quiz_start_kb() -> InlineKeyboardMarkup:
    """Quiz intro — single 'Start' button."""
    builder = InlineKeyboardBuilder()
    builder.button(text="▶️ Начать", callback_data="quiz_start")
    builder.button(text="🔙 Назад в меню", callback_data="menu")
    builder.adjust(1)
    return builder.as_markup()


def quiz_crm_kb() -> InlineKeyboardMarkup:
    """Q1 — does the user have a booking system?"""
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Да", callback_data="quiz_crm_yes")
    builder.button(text="❌ Нет", callback_data="quiz_crm_no")
    builder.adjust(2)
    return builder.as_markup()


def quiz_goal_kb() -> InlineKeyboardMarkup:
    """Q2 — what is the user's main goal?"""
    builder = InlineKeyboardBuilder()
    builder.button(text="📅 Автоматизировать запись", callback_data="quiz_goal_automate")
    builder.button(text="📈 Увеличить количество клиентов", callback_data="quiz_goal_grow")
    builder.button(text="🔧 Сделать всё под ключ", callback_data="quiz_goal_turnkey")
    builder.adjust(1)
    return builder.as_markup()


def quiz_lose_clients_kb() -> InlineKeyboardMarkup:
    """Q3 variant — do clients get lost before booking?"""
    builder = InlineKeyboardBuilder()
    builder.button(text="Да, есть такое", callback_data="quiz_detail_yes")
    builder.button(text="Иногда", callback_data="quiz_detail_sometimes")
    builder.button(text="Нет", callback_data="quiz_detail_no_lose")
    builder.adjust(1)
    return builder.as_markup()


def quiz_manual_kb() -> InlineKeyboardMarkup:
    """Q3 variant — does the user reply to clients manually?"""
    builder = InlineKeyboardBuilder()
    builder.button(text="Да", callback_data="quiz_detail_manual_yes")
    builder.button(text="Частично", callback_data="quiz_detail_manual_partial")
    builder.button(text="Нет", callback_data="quiz_detail_manual_no")
    builder.adjust(1)
    return builder.as_markup()


def quiz_result_kb() -> InlineKeyboardMarkup:
    """After quiz recommendation — apply or view all tariffs."""
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Выбрать этот тариф", callback_data="start_application")
    builder.button(text="💰 Посмотреть все тарифы", callback_data="tariffs")
    builder.adjust(1)
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
    builder.button(text="💎 START", callback_data="app_tariff_START")
    builder.button(text="🔥 GROW", callback_data="app_tariff_GROW")
    builder.button(text="💰 PRO", callback_data="app_tariff_PRO")
    builder.button(text="🤔 Нужна помощь с выбором", callback_data="app_tariff_Нужна помощь с выбором")
    builder.adjust(3, 1)
    return builder.as_markup()


def cancel_application_kb() -> InlineKeyboardMarkup:
    """Cancel button shown during free-text application steps."""
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Отменить заявку", callback_data="cancel_application")
    return builder.as_markup()
