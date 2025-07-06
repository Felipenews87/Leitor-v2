#!/data/data/com.termux/files/usr/bin/bash
cd ~/Leitor-v2 || exit
git add .
git commit -m "Bot auto update: $(date '+%Y-%m-%d %H:%M:%S')" || echo "Nada novo para commitar."
git push -u origin main
