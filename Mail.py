#!/usr/bin/env python
# encoding: utf-8


import smtplib
from email.mime.text import MIMEText


# MAil Config
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
SENDER = 'xxx.xxx@qq.com'
PASSWORD = 'xxx...'

RECIVER = ['xxx.xxx@qq.com']


class Mail(object):

    def send_mail(self, subject, content):
        text_subtype = 'plain'
        # 类型为utf-8, 否则客户端为乱码
        msg = MIMEText(content, text_subtype, 'utf-8')
        msg['Subject']= subject
        msg['From'] = SENDER

        mailserver = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login(SENDER, PASSWORD)

        mailserver.sendmail(SENDER, RECIVER, msg.as_string())

        mailserver.quit()


if __name__ == '__main__':
    mail = Mail()
    subject = 'Test subject'
    content = 'Test content'
    mail.send_mail(subject, content)
