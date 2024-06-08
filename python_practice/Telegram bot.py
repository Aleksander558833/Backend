import telebot
from util import ConvertionException, Exchanger
from config import keys, TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    text = (f'Здравствуй {message.chat.username}.'
            'Вас приветствует помощник по конвертации валюты.'
            'Как пользоваться данным ботом введите команду /help\n'            
            'Для просмотра доступных валют введите команду /values')
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = ('Что бы начать работу введите команду боту следующем образом:\n <имя валюты> '
            '<в какую валюту перевести> '
            '<количество переводимой валюты>')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) != 3:
        bot.reply_to(message, 'Слишком много или мало параметров. Ввдите команду /help для правильного ввода.')

    quote, base, amount = values
    try:
        total_base = Exchanger.exchange(quote, base, amount)
        text = f'Цена {amount} {quote} в {base} равно {total_base:.2f}.'
    except ConvertionException as ce:
        text = f'Ошибка конвертации: {ce}'
    except Exception as e:
        text = f'Неизвестная ошибка: {e}'

    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)


