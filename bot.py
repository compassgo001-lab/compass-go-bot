import os
import threading
from telebot import TeleBot, types
from flask import Flask, send_from_directory

# Инициализация Flask
app = Flask(__name__)
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

# ГЛАВНОЕ ИСПРАВЛЕНИЕ: Теперь по прямой ссылке будет открываться ваш index.html
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Используем вашу актуальную ссылку из Render
    web_app = types.WebAppInfo("https://compass-go-service.onrender.com") 
    item = types.KeyboardButton("Открыть CompassGo", web_app=web_app)
    markup.add(item)
    
    bot.send_message(
        message.chat.id, 
        "Добро пожаловать в CompassGo! Это лучший агрегатор и путеводитель международного уровня. Нажмите кнопку ниже для того чтобы запустить.", 
        reply_markup=markup
    )

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    threading.Thread(target=run_bot).start()
    # Запускаем веб-сервер на порту 10000 для Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
