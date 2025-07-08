import telebot

TELEGRAM_TOKEN = "7919510677:AAGU6d685TI7yKbhQ3MfnqImoLi7KrRZ7do"
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["diagnostico"])
def diagnostico(mensagem):
    bot.reply_to(mensagem, "✅ Bot está online e funcional!")

@bot.message_handler(commands=["ajuda"])
def ajuda(mensagem):
    resposta = (
        "🤖 Comandos disponíveis:\n"
        "/diagnostico - Verifica se o bot está online\n"
        "/ajuda - Mostra esta mensagem de ajuda\n"
    )
    bot.reply_to(mensagem, resposta)

bot.polling()

