import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import src.classe.user as user


class Email:
    def __init__(self, utilisateur: user.User):
        self.user = utilisateur.user
        self.serveur = self.user['smtp']['server']
        self.port = self.user['smtp']['port']
        self.login = self.user['smtp']['login']
        self.password = self.user['smtp']['password']
        self.email = utilisateur.email

    def envoyer(self, message, objet, isHtml, destinataire=""):
        # Définition du contexte de l'email
        msg = MIMEMultipart("alternative")
        msg['Subject'] = "[SecuPython]: {}".format(objet)
        msg['From'] = self.login
        msg['To'] = destinataire if destinataire != "" else self.email
        # Définition du type de contenu
        if isHtml:
            contenu = MIMEText(message, "html")
        else:
            contenu = MIMEText(message, "plain")
        # Ajout du contenu au mail
        msg.attach(contenu)
        # Lancement de la communication sécurisée
        ctx = ssl.create_default_context()
        try:
            # Requête d'envoi au serveur SMTP
            server = smtplib.SMTP(self.serveur, self.port)
            server.starttls(context=ctx)
            server.login(self.login, self.password)
            server.sendmail(self.login, destinataire if destinataire != "" else self.email, msg.as_string())
        except Exception as e:
            # Si la connexion échoue
            print(e)
        finally:
            # Fin de communication
            server.quit()
