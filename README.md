# 📧 Envio de E-mail Automático com Python (SMTP + Gmail)

Este projeto demonstra como enviar e-mails automaticamente usando Python e o servidor SMTP do Gmail. É ideal para tarefas de automação, como notificações, alertas ou envio programado de mensagens.

---

## 🧰 Tecnologias Utilizadas

- Python 3
- `smtplib` e `email.mime` (bibliotecas padrão do Python)
- `python-dotenv` (opcional, para segurança com variáveis de ambiente)

---

## ⚙️ Funcionalidades

- Conexão segura com servidor SMTP (`smtp.gmail.com`)
- Envio de e-mail com assunto e corpo personalizados
- Suporte a variáveis de ambiente para proteger dados sensíveis

---

## 🛡️ Segurança

**⚠️ Nunca exponha senhas ou e-mails diretamente no código.**  
Este projeto usa variáveis de ambiente para proteger suas credenciais.

---

## 📁 Estrutura do Projeto
send_email_automation.py
README.md


## 📦 Pré-requisitos
- Conta no Gmail com autenticação por senha de app ativada  
  *(acesse: [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords))*
- Python instalado
- (Opcional) Instalar `python-dotenv`:
pip install python-dotenv

🔧 Como Usar
Clone o repositório:

git clone https://github.com/seuusuario/enviar-email-python.git
cd enviar-email-python
Crie um arquivo .env com suas variáveis:

EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_senha_de_app
EMAIL_DESTINO=email_destinatario@gmail.com
Execute o script:


python send_email_automation.py
✅ Exemplo de uso
enviar_email(
    'Relatório Diário',
    'Olá! Este é o relatório diário gerado automaticamente.'
)
🧠 Observações
Se seu Gmail estiver com autenticação em dois fatores, você deve gerar uma senha de app.

Caso use outra plataforma de e-mail (Outlook, Yahoo, etc.), substitua o SMTP_SERVER e SMTP_PORT conforme a documentação do provedor.

📌 Licença
Este projeto é apenas educacional. Sem garantias ou suporte oficial.

✍️ Autor
Rodrigo Assarice
