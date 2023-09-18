#!/bin/sh

#$1 nome do arquivo

if [ -z "$1" ]; then
    echo "No filename provided."
    exit 1
fi

# O shell irá encerrar a execução do script quando um comando falhar
set -e

cd leitores/

mv "$1.docx" "$1.zip"
unzip -o "$1.zip" -d "./$1"
cd "$1/word/media"


if ls *.wmf 1> /dev/null 2>&1; then
    mogrify -format png *.wmf 
    mv *.png ../../../../media/questoes
fi

cd ../../..

rm -r "$1"
mv "$1.zip" "$1.docx"