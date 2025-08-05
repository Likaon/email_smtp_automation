import smtplib
from email.mime.text import MIMEText
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

EMAIL = os.environ.get('email_remetente')
SENHA = os.environ.get('email_senha')
DESTINATARIO = os.environ.get('email_destino')

def enviar_email(assunto, mensagem):
    msg = MIMEText(mensagem)
    msg['Subject'] = assunto
    msg['From'] = EMAIL
    msg['To'] = DESTINATARIO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, SENHA)
        server.sendmail(EMAIL, DESTINATARIO, msg.as_string())

    print('Email enviado!')

if __name__ == '__main__':
    enviar_email('Teste de Email Automático', 'Esta é uma mensagem enviada automaticamente pelo script Python.')