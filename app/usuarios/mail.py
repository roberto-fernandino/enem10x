import smtplib as smtp
import os
from pathlib import Path
from email.message import Message
from usuarios.models import Account

# BASEDIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Mail jet api keys

api_key = os.getenv("MAILJET_PUB")
api_secret_key = os.getenv("MAILJET_PRIV")


def procura_email_com_newsletter() -> list:
    ''''
    Retorna todas as contas do banco de dados com newsletter ativado
    '''
    contas_com_newsletter_ativado = Account.objects.filter(is_newsletter=True)
    return contas_com_newsletter_ativado

def procura_email_template() -> str:
    """
    Procura emails na pasta BASEDIR/usuarios/emails
    """
    emails = os.listdir(f"{BASE_DIR}/usuarios/emails")
    return emails


def EnviarEmail(email_template, subject: str, destinatario:str) -> None:
    """Envia email"""
    emails = procura_email_template()

    with smtp.SMTP("in-v3.mailjet.com", 587) as server:
        server.starttls()
        server.login(api_key, api_secret_key)
        message = Message()
        message["Subject"] = subject
        message["From"] = "emaildoenem10x@example.com"
        message["To"] = destinatario
