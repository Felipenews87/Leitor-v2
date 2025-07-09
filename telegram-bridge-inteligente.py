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
    elif "quem é você" in msg:
        return "echo 'Sou o executor, braço direito do Theo.'"
    elif "meu usuário" in msg:
        return "whoami"
    elif "onde estou" in msg:
        return "pwd"
    else:
        return msg

def comando_perigoso(cmd):
    proibidos = ["rm -rf /", ":(){", "mkfs", "shutdown", "reboot"]
    return any(p in cmd for p in proibidos)

@bot.message_handler(commands=["start"])
def registrar_chat(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    bot.reply_to(message, "🤖 Ponte inteligente ativada com sucesso.")
    print(f"🔗 CHAT_ID registrado: {CHAT_ID}")

@bot.message_handler(func=lambda m: True)
def executar(message):
    global CHAT_ID
    CHAT_ID = message.chat.id
    cmd = interpretar(message.text)

    if comando_perigoso(cmd):
        bot.reply_to(message, "⛔ Comando bloqueado por segurança.")
        return

    try:
        saida = os.popen(cmd).read()
        if not saida:
            saida = "Comando executado sem saída."

        # salvar histórico
        historico_path = "/data/data/com.termux/files/home/Leitor-v2/comunicacao/historico.log"
        with open(historico_path, "a") as log:
            log.write(f"[{time.ctime()}] {cmd}\n")

        if len(saida) > 4000:
            caminho = "/data/data/com.termux/files/home/Leitor-v2/comunicacao/saida_grande.log"
            with open(caminho, "w") as f:
                f.write(saida)
            with open(caminho, "rb") as f:
                bot.send_document(message.chat.id, f)
        else:
            bot.reply_to(message, f"✅ Saída:\n{saida}")
    except Exception as e:
        bot.reply_to(message, f"❌ Erro:\n{e}")

bot.polling()
