import smtplib, ssl
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class CMailHandler:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = os.environ.get("SMTP_SERVER_NAME")
        self.sender_mail = os.environ.get("MAIL_SENDER")
        self.password = os.environ.get("MAIL_PASSWORD")

    def send(self, emails, subject, content):
        recieve = emails

        context = ssl.create_default_context()
        print("FUNCTION CALL")
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_mail, self.password)
            body = str(content)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(self.sender_mail, recieve, message)
