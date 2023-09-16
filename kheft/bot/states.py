from telebot.asyncio_handler_backends import State, StatesGroup


class Advertisement(StatesGroup):
    registration = State()
    rules = State()
    user_telegram_id = State()
    book_description = State()
    book_price = State()
