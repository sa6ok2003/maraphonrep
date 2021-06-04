from aiogram import types
from misc import dp, bot
import sqlite3
from aiogram.dispatcher import FSMContext
from .sqlit import update_user
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
time_1 = 120 #Отдых 2 минуты (120 сек)
time_2 = 60 #Отдых 1 минутa (60 сек)

video_vedenie = 'BAACAgIAAxkBAAMgYLjVRvlqRN0dpoJidyzLjcPx2NYAAocMAAKkhZFJXHG0VnsjkaEfBA'
video_vadik_1 = 'BAACAgIAAxkBAAM_YLjdkrgX1CcX_Yc1yf1xSZiV27MAAtINAAJ345BJe4Le_y0MPPgfBA'
video_vadik_2 = 'BAACAgIAAxkBAANdYLoNmFt-jfnFdJzHXz1gdxT2-5oAAtINAAJ345BJe4Le_y0MPPgfBA'
video_vadik_3 = 'BAACAgIAAxkBAANzYLoSMqHNRcR48jG58BggfM7KK9QAAigNAAJT8aBJ7BXulN76deUfBA' #1 часть
video_vadik_4 = 'BAACAgIAAxkBAAN0YLoSvVcAAW4diQqeUesd2vTZ3l_jAAIuDQACU_GgSUktYGNEAyybHwQ' #2 часть
video_vadik_5 = 'BAACAgIAAxkBAAN1YLoTOTeIK4TMicEUSHWaRwQTZMgAAgwRAAI0AahJI8VlRVX74zofBA' #3 часть
video_kolya = 'BAACAgIAAxkBAAN2YLoURWu19Oe73TkwOPIzbMC1U9UAAg4MAAL_GbFJLcVKGcTlAUYfBA'
video_konech = 'BAACAgIAAxkBAAOPYLpnI89bZlIup7GuuLd8fOXddtEAAqYLAAKBGNlJTeX3-AQ_QVcfBA' #Конец

video_note_zapusk = 'DQACAgIAAxkBAAMmYLjZeBFUWhJcV8SAOuxA80BVGg8AApITAAJT8ZhJCdTbpqihNH8fBA'

photo1 = "AgACAgIAAxkBAAMPYLjPDGf5JUNlPE5lcLzIJctVbacAAiaxMRsb8EhJTIRqP3dFtP195U2eLgADAQADAgADcwADBDQGAAEfBA" #Введение
photo2 = "AgACAgIAAxkBAAIBLGBHVQRTqqpiZu7mrO3L5UJ7UMiAAAKwsjEbTtU5SkVKRyiZPqVsdqd0ly4AAwEAAwIAA20AAxZZBwABHgQ"
photo_vtoroy_zabeg = 'AgACAgIAAxkBAAN4YLoVe_TvjMqB3oTbktvtBr1FOSAAAu-0MRv_GblJsRwHmvLe2jKBTwukLgADAQADAgADeQADp-EBAAEfBA'
photo_i_want_rezelt = "AgACAgIAAxkBAAOOYLoX3ZxljXnWHbvNCkiS3wb2nxsAAo22MRsBVslJN6KiRWkTAqxITsaiLgADAQADAgADeQADkEgDAAEfBA"


photo_vadik1 = 'AgACAgIAAxkBAAMoYLja36Ns0UQvIBieiVctWNKtk8EAAv20MRtT8ZhJwnSpDF65yfz8aBGkLgADAQADAgADeQADm8ABAAEfBA'
photo_vadik2 = 'AgACAgIAAxkBAANcYLoM2OPYAAG7evP4mYcG6ojJh5qnAAJusjEbU_GgSfFQyHSZEa6iLcJNoi4AAwEAAwIAA3kAA4PUAgABHwQ'
photo_vadik3 = 'AgACAgIAAxkBAANyYLoRj_f1YxhNQYrB053C549PVm0AAomyMRtT8aBJ-JapeOOpjHAxMg-iLgADAQADAgADeQADiN4CAAEfBA' #Танкист
photo_vadik_pezdyuk = 'AgACAgIAAxkBAAN3YLoUnZkksIeiNwABrFHCNexP4ZceAAJ8szEb_xmxSeHZ_Gt9g5qmiUIlpC4AAwEAAwIAA3kAA37GAQABHwQ' #Пездюк

animator_1 = 'CgACAgIAAxkBAAMSYLjTTKuXKDWnmXQ1QrFvE1I2s60AAhcNAAJT8aBJhg-FX2cYI-0fBA' #Обезьянка

voice1 = 'AwACAgIAAxkBAAN5YLoWYjBjghIExqrHocD3wvZCU3QAArELAALQ57lJdhrGxuAojQofBA'

class regs(StatesGroup):
    names = State()
    fnames = State()
    url_step = State()
    get_kod = State()

@dp.callback_query_handler(text='start_go')
async def start_go1(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='💥Накинуться и сожрать💥', callback_data='start_and_sochrat')
    markup.add(bat1)

    await bot.send_photo(chat_id=call.message.chat.id,photo=photo1,caption="""Такс, ну шооо чеснока немного 😏 

1) ГовноТок полон миражей, если говорить на простом, тик ток это удача) знания и фишки «реков» 
это мираж - обман)

2) Именно поэтому, абсолютно любой обучающий материал, связанный с заработком, или по прокачке ГовноТока полное 💩 

3) Дать знания, и на этом все👋🥺 
нееее я же Одноус 🥸 мне важно заложить в тебя идею, и верный вектор развития! 

Жми на кнопку, мне не терпится зарядить тебя 🤩""",reply_markup=markup)


@dp.callback_query_handler(text='start_and_sochrat')
async def start_2(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Telegram', callback_data='wath_in_telega')
    bat2 = types.InlineKeyboardButton(text='Youtube', url='https://youtu.be/YXw6f6DY0X0')
    markup.add(bat1,bat2)

    await bot.send_animation(chat_id=call.message.chat.id,thumb=animator_1,animation=animator_1,caption="""Где тебе удобно смотреть видео?""",reply_markup=markup)
    await regs.fnames.set()


@dp.callback_query_handler(text='wath_in_telega',state='*')
async def start_wath_in_telega(call: types.callback_query,state: FSMContext):
    await bot.send_video(chat_id=call.message.chat.id,caption='Введение в Марафон 🔥',video=video_vedenie)
    await regs.fnames.set()



@dp.message_handler(state=regs.fnames, content_types='text')
async def domashka_2(message: types.Message, state: FSMContext):
    if (message.text).lower() == 'запуск':
        markup = types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='🔥ЕБАШ🔥', callback_data='ebash')
        markup.add(bat1)

        await bot.send_video_note(chat_id=message.chat.id,video_note=video_note_zapusk,reply_markup=markup)
        await state.finish()

@dp.callback_query_handler(text='ebash')
async def start_ebash(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='⚡️Погнали⚡️', callback_data='pognali')
    markup.add(bat1)
    await bot.send_photo(call.message.chat.id,caption="""Первый забег

Передаю микрофон Вадиму 🤙

🧑🏼 Вадим - Воу воу, меньше слов больше дела, погнали 🚀🚀 

🥸 Одноус - Желаю удачи каждому, кто попробует пройти марафон.

Ооо ещё добавлю!
Если возникнут проблемы, то пишите Вадику в инстаграм - 
https://instagram.com/vadiktiktok""",photo=photo_vadik1,reply_markup=markup)

@dp.callback_query_handler(text='pognali')
async def start_pognali(call: types.callback_query,state: FSMContext):
    await regs.names.set()
    await bot.send_video(chat_id=call.message.chat.id,video=video_vadik_1)

    await asyncio.sleep(time_1) # Отдых 2 минуты

    await bot.send_message(chat_id=call.message.chat.id,text="""1) Сервис по покупке тик ток аккаунтов, если нет других вариантов: <b><a href = "https://accsmarket.com/?ref=219675">asssmarket.com</a></b>

2) Инстаграм Николы: 
https://instagram.com/nikolanext

3) Канал с аватарками Николы: 
https://t.me/avausa

Задание! 
Прислать скриншот готового аккаунта тик ток, как показано на видео.

Отправляй прям сюда в бота😉""",parse_mode='html',disable_web_page_preview=True)

@dp.message_handler(state=regs.names, content_types=['photo','file','document'])
async def dsdafdsa(message: types.Message, state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='⚡️Погнали⚡️', callback_data='pognali_2')
    markup.add(bat1)
    await bot.send_photo(chat_id=message.chat.id,caption="""🤬 Боль - это когда потратил время впустую!

Что этого не было, погнали проверять наши аккаунты, на продуктивность!""",photo=photo_vadik2,reply_markup=markup)
    await state.finish()


@dp.callback_query_handler(text='pognali_2')
async def start_pognali_2(call: types.callback_query,state: FSMContext):
    await bot.send_video(chat_id=call.message.chat.id,video=video_vadik_2)
    await asyncio.sleep(time_2)
    await bot.send_message(chat_id=call.message.chat.id,text="""<b>Задание!</b>

📢 После того как наш ролик набрал 100 просмотров, отправляй ссылку ролика в бота.

🔞 Если ролик не набрал просмотры, создаём новый аккаунт, пробуем пока не получиться, сдаваться 100% не стоит!

Возникли трудности пиши мне👇
https://instagram.com/vadiktiktok""",parse_mode='html')
    await regs.url_step.set()

@dp.message_handler(state=regs.url_step, content_types=['text'])
async def dsdafdsa123(message: types.Message, state: FSMContext):
    if (message.text[0:15]) == 'https://vm.tikt' or message.text[0:8] == 'tiktok.c':
        markup = types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='⚔️ В бой ⚔️', callback_data='v_boy')
        markup.add(bat1)
        await bot.send_photo(chat_id=message.chat.id,photo=photo_vadik3,caption="""Мы полностью заряжены, пора  начинать войну, с тик током!

Жми на кнопку, и погнали 🚀""",reply_markup=markup)
        await state.finish()
    else:
        await bot.send_message(chat_id=message.chat.id,text='Не хитри! Отправляй ссылку на свой ролик, который набрал хотя бы 100 просмотров!')


@dp.callback_query_handler(text='v_boy')
async def v_boy(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Далее', callback_data='continuyu_1')
    markup.add(bat1)

    await bot.send_video(chat_id=call.message.chat.id,caption="""🤜💥 1 часть 💥🤛""",video=video_vadik_3,reply_markup=markup)

@dp.callback_query_handler(text='continuyu_1')
async def continuyu_1(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Далее', callback_data='continuyu_2')
    markup.add(bat1)

    await bot.send_video(chat_id=call.message.chat.id, caption="""🤜💥 2  часть 💥🤛""", video=video_vadik_4,
                         reply_markup=markup)

@dp.callback_query_handler(text='continuyu_2')
async def continuyu_2(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Если БАН?', callback_data='if_ban')
    markup.add(bat1)

    await bot.send_video(chat_id=call.message.chat.id, caption="""🤜💥 3 часть 💥🤛

Задание

Переснять 10 роликов, после  отправить ссылку, на аккаунт мне в директ :
https://instagram.com/vadiktiktok

🔥 Канал с роликами:
https://t.me/joinchat/KkPeqxjHSYQzYjBi 

🔥 Канал с фотками Николы:
https://t.me/avausa""", video=video_vadik_5, reply_markup=markup)


@dp.callback_query_handler(text='if_ban')
async def if_ban(call: types.callback_query,state: FSMContext):
    await bot.send_video(call.message.chat.id,video=video_kolya)
    await bot.send_photo(call.message.chat.id,photo=photo_vadik_pezdyuk,caption="""Не забывай про <b>Задание!!!</b>

Вова с Вадиком ждут твои 10 роликов)

Инстаграм куда надо отправить ссылку на аккаунт, с десятью переснятыми роликами тут 👇
https://instagram.com/vadiktiktok

После проверки, мы дадим тебе код, для запуска второго забега, вперёд 🔥""",parse_mode='html')
    await regs.get_kod.set()


@dp.message_handler(state=regs.get_kod, content_types=['text'])
async def dsdafdsfdsfdsfds(message: types.Message, state: FSMContext):
    if message.text == '290996':
        markup = types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='🎙️ Голосовой 🎙️', callback_data='get_voice')
        markup.add(bat1)

        await bot.send_photo(message.chat.id,photo=photo_vtoroy_zabeg,caption="""Фишка, без которой я бы не смог делать миллионные просмотры, вытаскивать деньги с тик тока, да и вообще рассказывать тебе тут 😅

Запишу голосовой, на 8 минут, данный способ требует раскрытого пояснения, + мне хочется поделиться с тобой 🤗""",parse_mode='html',reply_markup=markup)
        await state.finish()

@dp.callback_query_handler(text='get_voice')
async def get_voice(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Далее', callback_data='dalee3')
    markup.add(bat1)

    await bot.send_voice(chat_id=call.message.chat.id,voice=voice1,reply_markup=markup)


@dp.callback_query_handler(text='dalee3')
async def dalee3(call: types.callback_query,state: FSMContext):
    markup = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='Результат', callback_data='rezelt_324')
    markup.add(bat1)

    await bot.send_photo(call.message.chat.id,caption="""Бррррррааааа🔥🔥🔥

Отдай все 100% и забери 1% не спрашивая, принцип правильных продаж!

Нельзя заработать в тик токе, пока не поймёшь, к чему все движется!

Я уже говорил, что нам нужны осознанные люди, иначе не о каких десятков 🍋 не может идти и речи)

Жми на <b>Результат</b>""",photo=photo_i_want_rezelt,parse_mode='html',reply_markup=markup)


@dp.callback_query_handler(text='rezelt_324')
async def rezelt_324(call: types.callback_query,state: FSMContext):
    await bot.send_video(chat_id=call.message.chat.id,video=video_konech,caption="""Смотреть на Ютубе:
https://youtu.be/5mtiCogrH7A

Мой телеграм - @nikolanext""")

    update_user(call.message.chat.id)