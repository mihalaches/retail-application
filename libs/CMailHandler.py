import smtplib, ssl

class CMailHandler:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = "mihalachesebi06@gmail.com"
        self.password = "vricepwonpiumbjx"

    def send(self, emails, subject, content):
        recieve = emails

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.sender_mail, self.password)
            body = str(content)
            message = f'Subject: {subject}\n\n{body}'
            server.sendmail(self.sender_mail, recieve, message)
