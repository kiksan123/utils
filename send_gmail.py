import smtplib
from email.mime.text import MIMEText
import urllib.request
import re

class sendGmail:
    # change x(input your account)
    username, password = 'xxxxx@gmail.com', 'xxxxxxxxxxxxx'

    def __init__(self, to, sub, body):
        host, port = 'smtp.gmail.com', 465
        msg = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to

        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.mail(self.username)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()


if __name__ == '__main__':
    to = 'to email address@gmail.com'
    sub = 'test'
    body = str("test example")
    sendGmail(to, sub, body)
