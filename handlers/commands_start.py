from aiogram import types
from misc import dp,bot
import sqlite3
from .sqlit import reg_user
from aiogram.dispatcher import FSMContext
from .sqlit import stata_user
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
t1 = 30 # ВРЕМЯ ЗАДЕРЖКИ ПЕРВОГО КРУГДЯША

photo_start = 'AgACAgIAAxkBAAMCYLjMj-TTlMX6fXfmxjAZUgRnKMEAAkS1MRs59EBJY71wNSKw26GyOIaiLgADAQADAgADcwAD84YCAAEfBA'# Нажал старт


video_note_1 = 'DQACAgIAAxkBAAMOYEcqCtnC95WsLzD3z5vKzLoVgR4AAsUMAAKA8DhKYYAYY68lwroeBA'
video_one  = 'BAACAgIAAxkBAAIBeWBIz-xwsxOTqoqBfirSzswu28SZAAJGCwACFd1ISl2Au9LiTOkmHgQ'

class st_reg(StatesGroup):
    st_name = State()
    st_fname = State()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message,state: FSMContext):
    reg_user(message.chat.id)
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='😬 НАКИНУТЬСЯ 😬', callback_data='start_go')
    markup.add(bat1)

    await bot.send_photo(message.chat.id,photo=photo_start,caption = """Аааааааааааааааа 🤩

Мне тут пришла индейка, показать в стиле марафонского обучения, как мы делаем грязь 😈 в тик токе 🤜🪨

Пройдя Марафон, у тебя будет четкое представление, о том как мы рубим капусту, а ещё ты сможешь попробовать присоединиться, и стать частью, чего-то гигантского 😱

🔻Подключайся в тему🔻""",reply_markup=markup)
