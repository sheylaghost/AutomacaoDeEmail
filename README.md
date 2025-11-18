# AutomacaoDeEmail

Automação de Email em Python
Sistema completo de automação para envio de emails utilizando Python, com suporte para Gmail, Outlook e Yahoo. Inclui funcionalidades para envio de emails simples, formatados em HTML, com anexos e para múltiplos destinatários.
Características

Envio de emails de texto simples
Suporte para emails formatados em HTML
Anexação de arquivos (PDF, imagens, documentos)
Envio para múltiplos destinatários
Personalização de mensagens por destinatário
Compatível com Gmail, Outlook/Hotmail e Yahoo
Validação automática de provedor de email

Requisitos

Python 3.6 ou superior
Bibliotecas padrão do Python (smtplib, email)

Não é necessário instalar bibliotecas externas, pois o projeto utiliza apenas módulos nativos do Python.
Instalação
Clone ou baixe o repositório:
bashgit clone https://github.com/seu-usuario/automacao-email.git
cd automacao-email
Ou simplesmente baixe o arquivo bot_email.py diretamente.
Configuração
Passo 1: Habilitar Verificação em Duas Etapas
Para utilizar senhas de aplicativo, você precisa ter a verificação em duas etapas ativada em sua conta de email.
Gmail:

Acesse https://myaccount.google.com/security
Localize "Verificação em duas etapas"
Ative se ainda não estiver habilitada

Outlook/Hotmail:

Acesse https://account.microsoft.com/security
Habilite a verificação em duas etapas

Passo 2: Gerar Senha de Aplicativo
Senhas de aplicativo são credenciais específicas que permitem que aplicativos acessem sua conta sem usar sua senha principal.
Gmail:

Acesse https://myaccount.google.com/apppasswords
Selecione "Outro (nome personalizado)"
Digite "Python Email Bot"
Clique em "Gerar"
Copie a senha de 16 caracteres (remova os espaços)

Outlook/Hotmail:

Acesse https://account.live.com/proofs/manage/additional
Localize "Segurança de aplicativos"
Clique em "Criar uma nova senha de aplicativo"
Copie a senha gerada

Passo 3: Configurar Credenciais
Edite o arquivo bot_email.py e localize a seção final do código:
pythonif __name__ == "__main__":
    # Configuração
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "suasenhaemum16caracteres"
Substitua:

seu_email@gmail.com pelo seu endereço de email real
suasenhaemum16caracteres pela senha de aplicativo gerada (sem espaços)

Uso
Executar o Exemplo Básico
bashpython bot_email.py
Este comando executará o exemplo configurado e enviará um email de teste para o endereço especificado.
Enviar Email Simples
pythonfrom bot_email import AutomacaoEmail

auto = AutomacaoEmail("seu_email@gmail.com", "sua_senha_app")

auto.enviar_email_simples(
    destinatario="destinatario@exemplo.com",
    assunto="Assunto do Email",
    mensagem="Corpo da mensagem"
)
Enviar Email HTML
pythonhtml_conteudo = """
<html>
  <body>
    <h1>Título</h1>
    <p>Conteúdo formatado em HTML</p>
  </body>
</html>
"""

auto.enviar_email_html(
    destinatario="destinatario@exemplo.com",
    assunto="Email Formatado",
    html=html_conteudo
)
Enviar Email com Anexo
pythonauto.enviar_email_com_anexo(
    destinatario="destinatario@exemplo.com",
    assunto="Relatório Mensal",
    mensagem="Segue em anexo o relatório.",
    arquivo_path="caminho/para/arquivo.pdf"
)
Enviar para Múltiplos Destinatários
pythonlista_emails = [
    "pessoa1@exemplo.com",
    "pessoa2@exemplo.com",
    "pessoa3@exemplo.com"
]

auto.enviar_para_multiplos(
    lista_destinatarios=lista_emails,
    assunto="Notificação Importante",
    mensagem="Mensagem para todos"
)
```

## Estrutura do Projeto
```
automacao-email/
├── bot_email.py           # Código principal
└── README.md              # Este arquivo
Segurança
Dados Armazenados Localmente

Credenciais de email (apenas em memória durante execução)
Nenhum dado é armazenado em disco permanentemente

Boas Práticas

Nunca compartilhe suas senhas de aplicativo
Não envie mais de 500 emails por dia (limite do Gmail)
Adicione delays entre envios em massa para evitar bloqueios
Use variáveis de ambiente para credenciais em produção
Nunca inclua credenciais em repositórios públicos

Dados Não Coletados

Senhas de email principais
Conteúdo de emails enviados
Informações de destinatários
Telemetria ou métricas de uso

Limitações

Gmail: aproximadamente 500 emails por dia
Outlook: aproximadamente 300 emails por dia
Yahoo: aproximadamente 500 emails por dia
Delays recomendados entre envios: 1-2 segundos

Solução de Problemas
Erro: Username and Password not accepted

Verifique se a verificação em duas etapas está ativada
Certifique-se de usar uma senha de aplicativo, não sua senha normal
Remova todos os espaços da senha de aplicativo
Gere uma nova senha de aplicativo e tente novamente

Erro: Connection refused

Verifique sua conexão com a internet
Confirme que o firewall não está bloqueando a porta 587
Tente novamente após alguns minutos

Email não recebido

Verifique a pasta de spam
Confirme que o endereço do destinatário está correto
Aguarde alguns minutos (pode haver atraso na entrega)

English

Python Email Automation

Complete email automation system using Python, supporting Gmail, Outlook, and Yahoo. Includes functionalities for sending simple emails, HTML-formatted emails, emails with attachments, and to multiple recipients.

Features

Send plain text emails

Support for HTML-formatted emails

Attach files (PDFs, images, documents)

Send to multiple recipients

Personalize messages for each recipient

Compatible with Gmail, Outlook/Hotmail, and Yahoo

Automatic email provider validation

Requirements

Python 3.6 or higher

Python standard libraries (smtplib, email)

No external libraries are needed, as the project only uses Python’s native modules.

Installation

Clone or download the repository:

git clone https://github.com/your-username/automacao-email.git
cd automacao-email


Or simply download the bot_email.py file directly.

Configuration
Step 1: Enable Two-Factor Authentication

To use app passwords, you must have two-factor authentication enabled on your email account.

Gmail:

Go to https://myaccount.google.com/security

Locate "2-Step Verification"

Enable it if not already active

Outlook/Hotmail:

Go to https://account.microsoft.com/security

Enable two-step verification

Step 2: Generate App Password

App passwords are special credentials that allow apps to access your account without using your main password.

Gmail:

Go to https://myaccount.google.com/apppasswords

Select "Other (Custom Name)"

Enter "Python Email Bot"

Click "Generate"

Copy the 16-character password (remove any spaces)

Outlook/Hotmail:

Go to https://account.live.com/proofs/manage/additional

Locate "App passwords"

Click "Create a new app password"

Copy the generated password

Step 3: Configure Credentials

Edit the bot_email.py file and find the final section of the code:

if __name__ == "__main__":
    # Configuration
    MY_EMAIL = "your_email@gmail.com"
    APP_PASSWORD = "your16charapppassword"


Replace:

your_email@gmail.com with your real email address

your16charapppassword with the generated app password (no spaces)

Usage
Run the Basic Example
python bot_email.py


This will execute the configured example and send a test email to the specified address.

Send a Simple Email
from bot_email import AutomacaoEmail

auto = AutomacaoEmail("your_email@gmail.com", "your_app_password")

auto.send_simple_email(
    recipient="recipient@example.com",
    subject="Email Subject",
    message="Email body content"
)

Send HTML Email
html_content = """
<html>
  <body>
    <h1>Title</h1>
    <p>HTML-formatted content</p>
  </body>
</html>
"""

auto.send_html_email(
    recipient="recipient@example.com",
    subject="Formatted Email",
    html=html_content
)

Send Email with Attachment
auto.send_email_with_attachment(
    recipient="recipient@example.com",
    subject="Monthly Report",
    message="Please find the report attached.",
    file_path="path/to/file.pdf"
)

Send to Multiple Recipients
email_list = [
    "person1@example.com",
    "person2@example.com",
    "person3@example.com"
]

auto.send_to_multiple(
    recipients_list=email_list,
    subject="Important Notification",
    message="Message for everyone"
)

Project Structure
automacao-email/
├── bot_email.py           # Main code
└── README.md              # This file

Security
Locally Stored Data

Email credentials are kept only in memory during execution

No data is permanently stored on disk

Best Practices

Never share your app passwords

Do not send more than 500 emails per day (Gmail limit)

Add delays between bulk sends to avoid being blocked

Use environment variables for credentials in production

Never include credentials in public repositories

Data Not Collected

Main email passwords

Content of sent emails

Recipient information

Telemetry or usage metrics

Limitations

Gmail: ~500 emails/day

Outlook: ~300 emails/day

Yahoo: ~500 emails/day

Recommended delays between sends: 1–2 seconds

Troubleshooting

Error: Username and Password not accepted

Ensure two-factor authentication is enabled

Use an app password, not your normal password

Remove all spaces from the app password

Generate a new app password and try again

Error: Connection refused

Check your internet connection

Make sure the firewall isn’t blocking port 587

Try again after a few minutes

Email not received

Check your spam folder

Confirm the recipient’s address is correct

Wait a few minutes (delivery may be delayed)
