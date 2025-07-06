#!/data/data/com.termux/files/usr/bin/bash

# Bot inteligente — versão 0.1
# Analisa e atualiza repositório automaticamente

cd ~/Leitor-v2 || exit

# 🧠 Aqui o bot poderia ler, modificar ou reagir a arquivos

# Salvar log de atividade
echo "Bot rodou às $(date '+%Y-%m-%d %H:%M:%S')" >> bot.log

# Commita e envia automaticamente
./deploy.sh

chmod +x bot.sh
./bot.sh


#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit

# Atualiza status com data e hora
echo "Última execução: $(date '+%Y-%m-%d %H:%M:%S')" > status.txt

# Commita e envia
./deploy.sh


#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit

# Atualiza status com data e hora
echo "Última execução: $(date '+%Y-%m-%d %H:%M:%S')" > status.txt

# Commita e envia
./deploy.sh


#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit

# Atualiza status com data e hora
echo "Última execução: $(date '+%Y-%m-%d %H:%M:%S')" > status.txt

# Commita e envia
./deploy.sh



nano ~/Leitor-v2/bot.sh
./auto-bot.sh




CTRL + O → Enter → CTRL + X
chmod +x bot.sh
./bot.sh
nano ~/Leitor-v2/auto-bot.sh
#!/data/data/com.termux/files/usr/bin/bash

# AUTO BOT LOOP - Atualiza o repositório a cada 5 minutos

while true; do
    echo "🔄 Executando bot às $(date '+%Y-%m-%d %H:%M:%S')"
    ~/Leitor-v2/bot.sh
    echo "⏳ Aguardando 5 minutos..."
    sleep 300
done
chmod +x auto-bot.sh

cd ~/Leitor-v2
./auto-bot.sh

cd ~ && mkdir -p Leitor-v2 && cd Leitor-v2 && echo '#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit
git add .
git commit -m "Bot auto update: $(date \'+%Y-%m-%d %H:%M:%S\')" || echo "Nada novo para commitar."
git push -u origin main
' > deploy.sh && echo '#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit
echo "Última execução: $(date \'+%Y-%m-%d %H:%M:%S\')" > status.txt
echo "Bot executado às $(date \'+%Y-%m-%d %H:%M:%S\')" >> bot.log
./deploy.sh
' > bot.sh && echo '#!/data/data/com.termux/files/usr/bin/bash

while true; do
    echo "🔄 Executando bot às $(date \'+%Y-%m-%d %H:%M:%S\')"
    ~/Leitor-v2/bot.sh
    echo "⏳ Aguardando 5 minutos..."
    sleep 300
done
' > auto-bot.sh && chmod +x deploy.sh bot.sh auto-bot.sh && ./auto-bot.sh



cd ~ && mkdir -p Leitor-v2 && cd Leitor-v2 && echo '#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit
git add .
git commit -m "Bot auto update: $(date \'+%Y-%m-%d %H:%M:%S\')" || echo "Nada novo para commitar."
git push -u origin main
' > deploy.sh && echo '#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit
echo "Última execução: $(date \'+%Y-%m-%d %H:%M:%S\')" > status.txt
echo "Bot executado às $(date \'+%Y-%m-%d %H:%M:%S\')" >> bot.log
./deploy.sh
' > bot.sh && echo '#!/data/data/com.termux/files/usr/bin/bash

while true; do
    echo "🔄 Executando bot às $(date \'+%Y-%m-%d %H:%M:%S\')"
    ~/Leitor-v2/bot.sh
    echo "⏳ Aguardando 5 minutos..."
    sleep 300
done
' > auto-bot.sh && chmod +x deploy.sh bot.sh auto-bot.sh && ./auto-bot.sh

^O
O

