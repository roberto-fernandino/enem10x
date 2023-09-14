FROM python:3.11.4-alpine


LABEL mantainer="romfernandino@gmail.com"


# Define PYTHONUNBUFFERED como 1/True para que os outputs do Python sejam enviados diretamente para o terminal,
# em vez de serem armazenados em um buffer para envio posterior ao terminal.
ENV PYTHONUNBUFFERED=1

COPY app /app
COPY scripts /scripts

WORKDIR /app

# A porta 8000 estará disponível para conexões externas ao container
# É a porta que vamos usar para o Django.

EXPOSE 8000

# RUN executa comandos em um shell dentro do container para construir a imagem.
# O resultado da execução do comando é armazenado no sistema de arquivos da 
# imagem como uma nova camada.
# Agrupar os comandos em um único RUN pode reduzir a quantidade de camadas da 
# imagem e torná-la mais eficiente.
RUN apk update && apk add gcc python3-dev libpq-dev musl-dev postgresql-dev netcat-openbsd imagemagick parallel
        

RUN ls -la /app &&  \
    python3 -m venv /venv &&\
    /venv/bin/pip install --upgrade pip &&\
    /venv/bin/pip install -r requirements.txt &&\
    adduser --disabled-password --no-create-home admin &&\
    mkdir -p /data/static && \
    mkdir -p /data/media && \
    chown -R admin:admin /data/static && \
    chown -R admin:admin /data/media && \
    chown -R admin:admin /venv && \
    chown -R admin:admin /scripts && \
    chown -R admin:admin /app  &&\
    chmod -R 755 /data/static && \
    chmod -R 755 /data/media && \
    chmod -R 755 /app/ && \
    chmod +x /scripts/commands.sh &&\
    chmod +x /scripts/zipextract.sh 
    

# Adcionando scripts e binarios da bin pra antes no PATH
ENV PATH="/scripts:/venv/bin:$PATH"

USER admin

CMD ["commands.sh"]


