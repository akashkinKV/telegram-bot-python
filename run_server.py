import flask
from telebot import types, TeleBot

import os
from twilio.rest import Client
server = flask.Flask(__name__)
from twilio.rest import Client

account_sid = 'AC52a194acef951b3b36e94f294d836ae6'
auth_token = '988090f0870502e26899be8b5aeb41f0'
bot = TeleBot('873656324:AAFqF5d_0oAMgN2F2XPW5xMjrGULZvUnZTI')
keyboard1 = types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
        client = Client(account_sid, auth_token)
        call = client.calls.create(
            url='https://ex.ru',
            to='+79162721765',
            from_='+12027967603',
            timeout='60'
        )
        print(call.sid)


    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)



if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling()
    server.run(host="localhost", port=int(os.environ.get('PORT', 5000)))


