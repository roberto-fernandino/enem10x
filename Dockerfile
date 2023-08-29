FROM python:3.11-slim-buster

# Define PYTHONUNBUFFERED como 1/True para que os outputs do Python sejam enviados diretamente para o terminal,
# em vez de serem armazenados em um buffer para envio posterior ao terminal.
ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


