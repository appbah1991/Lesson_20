import telebot
import requests
import pprint
from telebot import types #импорт клавиатуры
from telebot import util # Для разбивки большого текста на части


TOKEN = '5576487491:AAGzd3I9X_wNp7hsyrXqqlHgVMmVhq8eM50'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

# Информация о боте
url = f'{MAIN_URL}/getMe'

help_info_text = 'парсинг новостей с сайта - pythondigest.ru, парсит новости по запросу "java", на выходе получаем файл со словарями (заголовок новости, ссылка на новость, сама новость'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1, one_time_keyboard=True)
    yes = types.KeyboardButton(text = 'Yes')
    no = types.KeyboardButton(text = 'No')
    kb.add(yes, no)
    bot.send_message(message.chat.id, 'Приветсвую тебя, парсер готов к работе! Стартуем?', reply_markup=kb)


@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, help_info_text)

@bot.message_handler(commands = ['all'])
def all(message):
    admin_id = 1279593757
    if message.from_user.id == admin_id:
        list_of_news = open('list_of_news.txt', 'rb')
        bot.send_document(message.chat.id, list_of_news)
    else:
        bot.send_message(message.chat.id, 'Извните, у вас нет прав доступа((')

@bot.message_handler(func = lambda x: x.text == 'Yes' or x.text == 'No')
def start(message):
    if message.text == 'Yes':
        my_file = open('list_of_news.txt', 'rb')
        bot.send_message(message.chat.id, 'Парсер выполнил свою работу. Список новостей в файле')
        bot.send_document(message.chat.id, my_file)
    elif message.text == 'No':
        stiker_id = 'CAACAgIAAxkBAAMaYq9XmfJ5tQx9IkaQcD5qXrizOscAAn0TAAKjd6hLwlg7A4hvzeAkBA'
        bot.send_message(message.chat.id, 'Ок, заходи в следующий раз))')
        bot.send_sticker(message.chat.id, stiker_id)
bot.polling()