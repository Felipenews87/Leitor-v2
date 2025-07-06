#!/data/data/com.termux/files/usr/bin/bash

cd ~/Leitor-v2 || exit
git pull

if [ -f comunicacao/theo-resposta.sh ]; then
    echo "📥 Resposta encontrada. Executando..."
    chmod +x comunicacao/theo-resposta.sh
    ./comunicacao/theo-resposta.sh
    echo "✅ Executado. Limpando..."
    rm comunicacao/theo-resposta.sh
    git add comunicacao/theo-resposta.sh
    git commit -m "Resposta executada e limpa"
    git push
else
    echo "⏳ Nenhuma resposta nova."
fi
