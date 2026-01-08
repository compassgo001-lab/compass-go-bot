import os
import threading
from telebot import TeleBot, types
from flask import Flask

# Инициализация Flask для Render
app = Flask(__name__)
TOKEN = os.environ.get('BOT_TOKEN')
bot = TeleBot(TOKEN)

@app.route('/')
def health_check():
    return "Bot is alive!", 200

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Замените ссылку ниже на вашу реальную ссылку из Render
    web_app = types.WebAppInfo("https://compass-go-service.onrender.com") 
    item = types.KeyboardButton("Открыть CompassGo", web_app=web_app)
    markup.add(item)
    bot.send_message(message.chat.id, "Добро пожаловать! Нажмите кнопку ниже:", reply_markup=markup)

def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Запускаем бота в отдельном потоке
    threading.Thread(target=run_bot).start()
    # Запускаем Flask на порту, который требует Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
