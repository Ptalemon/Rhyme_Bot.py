from telebot import types
from multiprocessing import connection
from telegram_bot_pagination import InlineKeyboardPaginator
from telebot import util
import pymysql
import telebot

bot = telebot.TeleBot('6895605353:AAFHRHVWwOcXKE2bh4z2NrRvwmzuhYXbBmc')

@bot.message_handler(func= lambda message: True) #тип получаемых сообщений

def menu(message): #кнокпи
    bot.delete_message(message.chat.id, message.id)
    keyboard = types.InlineKeyboardMarkup()
    key_verbs = types.InlineKeyboardButton(text='Глаголы', callback_data='Verbs')
    keyboard.add(key_verbs)
    key_adjectives = types.InlineKeyboardButton(text='Прилагательные', callback_data='Adjectives')
    keyboard.add(key_adjectives)
    key_nouns = types.InlineKeyboardButton(text='Существительные', callback_data='Nouns')
    keyboard.add(key_nouns)
    question = 'Какой тип речи изволите?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda callback: callback.data) #стартуем ответ

def callback_worker(call): #Ответочка идёт в зависимости от нажатой кнопки
    if call.data == 'Adjectives':
        bot.delete_message(call.message.chat.id, call.message.id) #удаляем сообщение с кнопками. На компе даже с изменённым сообщением остаются кнопки
        bot.send_message(call.from_user.id, text='Вспоминаю прилагательные...')
    if call.data == 'Verbs':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.from_user.id, text='Вспоминаю глаголы...')
    if call.data == 'Nouns':
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.from_user.id, text='Вспоминаю существительные...')

    
bot.polling(none_stop=True, interval=0)