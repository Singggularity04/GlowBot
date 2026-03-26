# GlowBot — Telegram-бот для бизнеса

Telegram-бот для приёма заявок, FAQ, выбора тарифов и прогрева клиентов.  
Создан для бизнеса **GlowBot** — автоматизация общения с клиентами.

## Возможности

- 🤖 Автоматические ответы на частые вопросы
- 💰 Отображение тарифов с подбором
- 📝 Сбор заявок через 6-шаговый сценарий
- 🔔 Уведомление админа о новых заявках
- 💬 Quick-reply ответы на типовые сообщения
- ❓ FAQ-раздел с кнопками

## Установка

1. Клонировать репозиторий
2. Создать виртуальное окружение:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate  # Linux/Mac
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Создать файл `.env` на основе `.env.example`:
   ```
   BOT_TOKEN=ваш_токен_от_BotFather
   ADMIN_CHAT_ID=ваш_telegram_id
   ```
   > **Как узнать ADMIN_CHAT_ID:** напишите боту [@userinfobot](https://t.me/userinfobot) в Telegram.

5. Запустить бота:
   ```bash
   python bot.py
   ```

## Структура проекта

```
├── bot.py              # Точка входа
├── config.py           # Загрузка переменных окружения
├── handlers/
│   ├── start.py        # /start и главное меню
│   ├── info.py         # О ботах, как работает, контакты
│   ├── tariffs.py      # Тарифы и подбор
│   ├── faq.py          # Частые вопросы
│   ├── application.py  # FSM-заявка (6 шагов)
│   └── quick_replies.py # Авто-ответы на сообщения
├── keyboards/
│   └── inline.py       # Все inline-клавиатуры
├── texts/
│   └── messages.py     # Все тексты бота
├── .env.example
├── requirements.txt
└── README.md
```
