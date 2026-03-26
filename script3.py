import telebot
from telebot import types
bot=telebot.TeleBot(token='8404833686:AAHtSQembw_5DT01fXEzvhYFLkkykkE1-54')
@bot.message_handler(content_types=['photo','sticker','document','video','audio','voice'])
def send_photo(message):
    bot.send_message(chat_id=message.chat.id,text="Эй,эот бот НИКАК не может работать с этим типом данных")
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(message.chat.id, 'https://ibb.co/DHxfp8FZ')
    bot.send_message(chat_id=message.chat.id, text="Привет! Я получил команду /start нажми на /help для получения всех функций")
@bot.callback_query_handler(func=lambda call: call.data == 'send_stk')
def callback_sticker(call):
    bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEQ0sVpxWFB0-QDr4Hl5EDYKDShk679fgACwF0AAoqOEUn74TsHxbsyAjoE')
@bot.message_handler(commands=['knopka'])
def send_knopka(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("кнопка",callback_data='send_stk'))
    bot.reply_to(message,'нажми на кнопку',reply_markup=markup)
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(chat_id=message.chat.id, text="Привет! Я получил команду /help нажми на /knopka для жмака на кнопку, /ricrol для рикрола, /Zashita для защиты от дебила")
@bot.message_handler(commands=['ricrol'])
def send_ricrol(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("рикрол", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    bot.send_message(chat_id=message.chat.id, text='нижимай на кнопку', reply_markup=markup)
    bot.send_message(chat_id=message.chat.id, text='зарикролен)))')
@bot.message_handler(commands=['Zashita'])
def send_zashita(message):
    bot.send_message(chat_id=message.chat.id, text='В этот бот встроена"защита от дебила" если юзер отправляет видео, фото или другое мультимедиа бот говорит что не может работать с таким типом данных')
bot.infinity_polling()
