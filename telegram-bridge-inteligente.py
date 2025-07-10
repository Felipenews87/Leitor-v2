import os
import telebot
import time
import re

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    print("Erro: A variável de ambiente TELEGRAM_BOT_TOKEN não está definida.")
    exit(1)

bot = telebot.TeleBot(TOKEN)
CHAT_ID = None

def interpretar(msg):
    msg = msg.lower()
    if "listar" in msg and "arquivo" in msg:
        return "ls -la"
    elif "atualizar" in msg:
        return "pkg update -y && pkg upgrade -y"
    elif "apagar" in msg:
        arquivo = msg.split("apagar")[-1].strip()
        return f"rm -f {arquivo}"
    return msg

@bot.message_handler(commands=['start', 'ajuda'])
def boas_vindas(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.reply_to(message, "🤖 Ponte inteligente ativada com sucesso.")

@bot.message_handler(commands=['diagnóstico'])
def diagnostico(message):
    try:
        cmd = "bash ./scripts/diagnostico.sh"
        saida = os.popen(cmd).read()
        if not saida:
            saida = "Comando executado sem saída."
        if len(saida) > 4000:
            caminho = "./comunicacao/historico.log"
            with open(caminho, "w") as f:
                f.write(saida)
            with open(caminho, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.reply_to(message, f"✅ Saída:\n{saida}")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro:\n{e}")

@bot.message_handler(func=lambda m: True)
def terminal(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    try:
        cmd = interpretar(message.text)
        saida = os.popen(cmd).read()
        if not saida:
            saida = "Comando executado sem saída."
        if len(saida) > 4000:
            caminho = "./comunicacao/historico.log"
            with open(caminho, "w") as f:
                f.write(saida)
            with open(caminho, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.reply_to(message, f"✅ Saída:\n{saida}")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro:\n{e}")

print("🔗 CHAT_ID registrado:", CHAT_ID)
bot.polling()
