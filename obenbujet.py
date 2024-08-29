from aiogram.types import Message, ChatType
from aiogram import Bot, Dispatcher, executor
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot('7288386568:AAFe4Gx-_NjN1l31vr4xkOLhw1qgO-TUJfA')
dp = Dispatcher(bot)


kinopka = InlineKeyboardMarkup()
kinopka.add(
    InlineKeyboardButton(text='ovoz berish',
                         url='https://t.me/ochiqbudjet_07_bot?start=048335086011')
    )


@dp.message_handler(commands=['start'])
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid,
                           text='Xush kelibsiz.Ovoz berish uchun kinplani bosing.',
                           reply_markup=kinopka)




executor.start_polling(dp, skip_updates=True)