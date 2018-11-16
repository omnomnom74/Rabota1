import os

from flask import Flask, request

import telebot

TOKEN = '772991352:AAH7AyNGIpG1-UAKFx3_s6MKOwU25Ikvkls'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    # bot.reply_to(message, message.text)

    if message.text == 'Кто самый лучший человек на земле?':
        bot.send_message(message.chat.id, 'Соня- самый лучший человек на земле <3')
    else:
        bot.send_message(message.chat.id, 'Задай правильный вопрос:\n"Кто самый лучший человек на земле?"')


# @server.route('/' + TOKEN, methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200


# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
#     return "!", 200
#
#
# if __name__ == "__main__":
#     server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
#
bot.polling()
