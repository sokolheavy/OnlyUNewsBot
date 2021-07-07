from flask import Flask, request
import keys as keys
import responses as R
import telebot
from telebot import types
from personal_news.extract_keywords import get_keywords
import time

app = Flask(__name__)
bot = telebot.TeleBot(keys.get_telegram_key())
bot.set_webhook(url="https://api.telegram.org/bot1802980510:AAFBDo0qL3PWiIeMGsok73EBuHa0TKS8R0M/setWebhook?url=https://47a5cabbf897.ngrok.io")


@app.route('/{}'.format("GUID"), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Personal', 'By keywords')
    msg = bot.send_message(message.chat.id, "Helloes, I`m @OnlyUNewsBot! \nCan give you special news only for you!👌\nWhich news are you prefer?", reply_markup=markup)
    bot.register_next_step_handler(msg, welcome_step_first)

def welcome_step_first(message):
    if message.text=='By keywords':
        response = "Please, write the keywords"
        msg = bot.send_message(message.chat.id, response)
        bot.register_next_step_handler(msg, welcome_step_second)
    if message.text == 'Personal':
        chat_id = message.chat.id
        response_news = R.keyword_responses(get_keywords())
        bot.send_message(chat_id, response_news)


def welcome_step_second(message):
    chat_id = message.chat.id
    response_news = R.keyword_responses(message.text)
    bot.send_message(chat_id, response_news)


@bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "✨ Magic words:\n\n  /start - start working with the bot; \n /personal - get personal news; \n /keywords - get news by keywords;")


@bot.message_handler(commands=["keywords"])
def send_messages_by_keywords(message):
    response = "Please, write the keywords"
    msg = bot.send_message(message.chat.id, response)
    bot.register_next_step_handler(msg, send_messages_by_keywords_step_second)


def send_messages_by_keywords_step_second(message):
    chat_id = message.chat.id
    response_news = R.keyword_responses(message.text)
    bot.send_message(chat_id, response_news)


@bot.message_handler(commands=["personal"])
def send_messages_personal(message):
    chat_id = message.chat.id
    response_news = R.keyword_responses(get_keywords())
    bot.send_message(chat_id, response_news)


@bot.message_handler(content_types=["text"])
def send_messages_text(message):
    chat_id = message.chat.id
    response_news = R.sample_responses(message.text)
    bot.send_message(chat_id, response_news)



if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)


