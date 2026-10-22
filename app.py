import os
import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Твой токен от BotFather
TOKEN = '8815423174:AAHUIAsgZyURtSPg6i-_e5NQcR1OHipHVj4'
bot = telebot.TeleBot(TOKEN)

WEBAPP_URL = 'https://google.com'

@bot.message_handler(commands=['start'])
def start_message(message):
    # Создаем кнопку
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="🎴 Открыть Альбом Карточек", web_app=WebAppInfo(url=WEBAPP_URL)))
    
    bot.send_message(
        message.chat.id, 
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в игру по сбору хоккейных карточек КХЛ!\n"
        "Жми на кнопку ниже, чтобы начать.", 
        reply_markup=markup
    )

print("Бот запущен...")
bot.infinity_polling()
