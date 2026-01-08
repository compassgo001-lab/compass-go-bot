import os
from telebot import TeleBot, types
from flask import Flask

# Берем токен из настроек Render (Environment Variables)
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Название кнопки, которая откроет ваше приложение
    web_app = types.WebAppInfo("https://ВАШ-URL-ИЗ-RENDER.onrender.com") 
    item = types.KeyboardButton("Открыть CompassGo", web_app=web_app)
    markup.add(item)
    
    bot.send_message(message.chat.id, "Добро пожаловать в CompassGo! Нажмите на кнопку ниже, чтобы начать.", reply_markup=markup)

# Это нужно для того, чтобы Render не выдавал ошибку портов
@app.route('/')
def index():
    return "Bot is running"

if __name__ == "__main__":
    # Запускаем бота
    bot.infinity_polling()
