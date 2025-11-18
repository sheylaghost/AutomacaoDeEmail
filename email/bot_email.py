import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

class AutomacaoEmail:
    """
    Classe para automação de envio de emails
    Suporta Gmail, Outlook, Yahoo e outros
    """
    
    def __init__(self, email_remetente, senha):
        """
        Inicializa o automatizador de email
        
        Args:
            email_remetente: Seu endereço de email
            senha: Sua senha de aplicativo (não a senha normal!)
        """
        self.email_remetente = email_remetente
        self.senha = senha
        
        # Configurações de servidor SMTP por provedor
        self.servidores_smtp = {
            'gmail.com': ('smtp.gmail.com', 587),
            'outlook.com': ('smtp-mail.outlook.com', 587),
            'hotmail.com': ('smtp-mail.outlook.com', 587),
            'yahoo.com': ('smtp.mail.yahoo.com', 587),
        }
        
        # Detectar provedor
        dominio = email_remetente.split('@')[1]
        if dominio in self.servidores_smtp:
            self.servidor, self.porta = self.servidores_smtp[dominio]
        else:
            raise ValueError(f"Provedor {dominio} não configurado. Use Gmail, Outlook ou Yahoo.")
    
    def enviar_email_simples(self, destinatario, assunto, mensagem):
        """
        Envia um email de texto simples
        
        Args:
            destinatario: Email do destinatário
            assunto: Assunto do email
            mensagem: Corpo do email (texto)
        
        Returns:
            True se enviado com sucesso, False caso contrário
        """
        try:
            # Criar mensagem
            msg = MIMEMultipart()
            msg['From'] = self.email_remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            
            # Adicionar corpo do email
            msg.attach(MIMEText(mensagem, 'plain'))
            
            # Conectar ao servidor e enviar
            with smtplib.SMTP(self.servidor, self.porta) as server:
                server.starttls()  # Segurança
                server.login(self.email_remetente, self.senha)
                server.send_message(msg)
            
            print(f"✅ Email enviado para {destinatario}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar email: {e}")
            return False
    
    def enviar_email_html(self, destinatario, assunto, html):
        """
        Envia um email com HTML (formatado)
        
        Args:
            destinatario: Email do destinatário
            assunto: Assunto do email
            html: Conteúdo HTML do email
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email_remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            
            # Adicionar versão HTML
            parte_html = MIMEText(html, 'html')
            msg.attach(parte_html)
            
            # Enviar
            with smtplib.SMTP(self.servidor, self.porta) as server:
                server.starttls()
                server.login(self.email_remetente, self.senha)
                server.send_message(msg)
            
            print(f"✅ Email HTML enviado para {destinatario}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar email HTML: {e}")
            return False
    
    def enviar_email_com_anexo(self, destinatario, assunto, mensagem, arquivo_path):
        """
        Envia email com arquivo anexo
        
        Args:
            destinatario: Email do destinatário
            assunto: Assunto do email
            mensagem: Corpo do email
            arquivo_path: Caminho do arquivo a ser anexado
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_remetente
            msg['To'] = destinatario
            msg['Subject'] = assunto
            
            # Corpo do email
            msg.attach(MIMEText(mensagem, 'plain'))
            
            # Anexar arquivo
            if os.path.exists(arquivo_path):
                nome_arquivo = os.path.basename(arquivo_path)
                
                with open(arquivo_path, 'rb') as anexo:
                    parte = MIMEBase('application', 'octet-stream')
                    parte.set_payload(anexo.read())
                
                encoders.encode_base64(parte)
                parte.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {nome_arquivo}'
                )
                msg.attach(parte)
            else:
                print(f"⚠️ Arquivo não encontrado: {arquivo_path}")
                return False
            
            # Enviar
            with smtplib.SMTP(self.servidor, self.porta) as server:
                server.starttls()
                server.login(self.email_remetente, self.senha)
                server.send_message(msg)
            
            print(f"✅ Email com anexo enviado para {destinatario}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao enviar email com anexo: {e}")
            return False
    
    def enviar_para_multiplos(self, lista_destinatarios, assunto, mensagem):
        """
        Envia o mesmo email para múltiplos destinatários
        
        Args:
            lista_destinatarios: Lista de emails dos destinatários
            assunto: Assunto do email
            mensagem: Corpo do email
        """
        enviados = 0
        falhas = 0
        
        for destinatario in lista_destinatarios:
            if self.enviar_email_simples(destinatario, assunto, mensagem):
                enviados += 1
            else:
                falhas += 1
        
        print(f"\n📊 Resumo: {enviados} enviados, {falhas} falhas")
        return enviados, falhas


# ============================================
# EXEMPLOS DE USO
# ============================================

def exemplo_email_simples():
    """Exemplo: Email de texto simples"""
    
    # CONFIGURAÇÃO - MUDE AQUI!
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "sua_senha_de_aplicativo"  # NÃO é a senha normal!
    
    # Criar automatizador
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    # Enviar email
    auto.enviar_email_simples(
        destinatario="destinatario@exemplo.com",
        assunto="Teste de Automação",
        mensagem="Olá! Este é um email enviado automaticamente com Python! 🐍"
    )


def exemplo_email_html():
    """Exemplo: Email formatado com HTML"""
    
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "sua_senha_de_aplicativo"
    
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    html = """
    <html>
      <body style="font-family: Arial, sans-serif;">
        <h2 style="color: #4CAF50;">Relatório Diário 📊</h2>
        <p>Olá!</p>
        <p>Segue o relatório de hoje:</p>
        <ul>
          <li><strong>Vendas:</strong> R$ 15.000</li>
          <li><strong>Novos clientes:</strong> 23</li>
          <li><strong>Status:</strong> <span style="color: green;">✅ Tudo OK</span></li>
        </ul>
        <p>Atenciosamente,<br><strong>Sistema Automático</strong></p>
      </body>
    </html>
    """
    
    auto.enviar_email_html(
        destinatario="destinatario@exemplo.com",
        assunto="Relatório Diário",
        html=html
    )


def exemplo_email_com_anexo():
    """Exemplo: Email com arquivo anexo"""
    
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "sua_senha_de_aplicativo"
    
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    auto.enviar_email_com_anexo(
        destinatario="destinatario@exemplo.com",
        assunto="Relatório Mensal",
        mensagem="Segue em anexo o relatório mensal.",
        arquivo_path="relatorio.pdf"  # Caminho do arquivo
    )


def exemplo_multiplos_destinatarios():
    """Exemplo: Enviar para várias pessoas"""
    
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "sua_senha_de_aplicativo"
    
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    lista_emails = [
        "pessoa1@exemplo.com",
        "pessoa2@exemplo.com",
        "pessoa3@exemplo.com"
    ]
    
    auto.enviar_para_multiplos(
        lista_destinatarios=lista_emails,
        assunto="Newsletter Semanal",
        mensagem="Confira as novidades desta semana!"
    )


def exemplo_email_personalizado():
    """Exemplo: Email personalizado para cada pessoa"""
    
    MEU_EMAIL = "seu_email@gmail.com"
    SENHA_APP = "sua_senha_de_aplicativo"
    
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    # Lista com dados personalizados
    clientes = [
        {"nome": "João", "email": "joao@exemplo.com", "valor": 1500},
        {"nome": "Maria", "email": "maria@exemplo.com", "valor": 2300},
        {"nome": "Pedro", "email": "pedro@exemplo.com", "valor": 890}
    ]
    
    for cliente in clientes:
        mensagem = f"""
Olá {cliente['nome']}!

Seu pedido no valor de R$ {cliente['valor']:.2f} foi aprovado! 🎉

Obrigado pela preferência.

Atenciosamente,
Equipe de Vendas
        """
        
        auto.enviar_email_simples(
            destinatario=cliente['email'],
            assunto=f"Pedido Aprovado - {cliente['nome']}",
            mensagem=mensagem
        )


# ============================================
# EXECUTAR EXEMPLO
# ============================================

if __name__ == "__main__":
    print("🚀 Automação de Email - Python")
    print("=" * 50)
    
    # CONFIGURAÇÃO - MUDE AQUI! ⬇️⬇️⬇️
    MEU_EMAIL = "eyshilaivanha@gmail.com"  # ⬅️ Coloque seu email aqui
    SENHA_APP = "ijhzfbhiddhbzpvh"  # ⬅️ Cole sua senha de app aqui
    
    # Criar automatizador
    auto = AutomacaoEmail(MEU_EMAIL, SENHA_APP)
    
    # Enviar email de teste (para você mesmo)
    auto.enviar_email_simples(
        destinatario="eyshilaivanha@gmail.com",  # ⬅️ Seu email de novo
        assunto="Teste Python - Funcionou! 🎉",
        mensagem="Olá! Este email foi enviado automaticamente com Python! 🐍\n\nSe você recebeu isso, a automação está funcionando!"
    )
    
    print("\n✅ Verifique sua caixa de entrada!")
    
    # OU descomente um dos exemplos abaixo:
    # exemplo_email_simples()
    # exemplo_email_html()
    # exemplo_email_com_anexo()
    # exemplo_multiplos_destinatarios()
    # exemplo_email_personalizado()