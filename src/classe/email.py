import src.classe.user as user
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Email:
    def __init__(self, utilisateur: user.User):
        self.user = utilisateur.user
        self.serveur = self.user['smtp']['server']
        self.port = self.user['smtp']['port']
        self.login = self.user['smtp']['login']
        self.password = self.user['smtp']['password']
        self.email = utilisateur.email

    def envoyer(self, message, isHtml):
        msg = MIMEMultipart("alternative")
        msg['Subject'] = "[SecuPython]: Alerte tentative de connexion"
        msg['From'] = self.login
        msg['To'] = self.email
        if isHtml:
            contenu = MIMEText(message, "html")
        else:
            contenu = MIMEText(message, "plain")
        msg.attach(contenu)
        ctx = ssl.create_default_context()
        try:
            server = smtplib.SMTP(self.serveur, self.port)
            server.starttls(context=ctx)
            server.login(self.login, self.password)
            server.sendmail(self.login, self.email, message.as_string())
        except Exception as e:
            print(e)
        finally:
            server.quit()
