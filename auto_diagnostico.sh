#!/bin/bash
LOGFILE=~/Leitor-v2/diagnostico.log
echo "=== Diagnóstico em $(date) ===" > $LOGFILE

echo "Espaço em disco:" >> $LOGFILE
df -h >> $LOGFILE

echo "Memória livre:" >> $LOGFILE
free -h >> $LOGFILE

echo "Processos Python ativos:" >> $LOGFILE
ps aux | grep python | grep -v grep >> $LOGFILE

echo "Últimas 20 linhas do log do bot:" >> $LOGFILE
tail -n 20 ~/Leitor-v2/bot.loge EOF
