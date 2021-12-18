import src.emailContent as emailContent
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, user):
        self.server = user['smtp']['server']
        self.port = user['smtp']['port']
        self.login = user['smtp']['login']
        self.password = user['smtp']['password']
        self.email = user['default-email']

    def envoyer(self):
        message = MIMEMultipart("alternative")
        message['Subject'] = "[SecuPython]: Alerte tentative de connexion"
        message['From'] = self.login
        message['To'] = self.email
        html = emailContent.html

        html_mime = MIMEText(html, 'html')
        message.attach(html_mime)
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP(self.server, self.port)
            server.starttls(context=context)
            server.login(self.login, self.password)
            server.sendmail(self.login, self.email, message.as_string())
        except Exception as e:
            print(e)
        finally:
            server.quit()
