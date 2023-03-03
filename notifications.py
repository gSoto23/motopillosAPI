import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(email_receiver, subject, html_body):
    email_sender = 'motopillos@gmail.com'
    email_password = 'slcltdcuihducqil'
    cc_receiver = 'motopillos@gmail.com'

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = email_sender
    msg["To"] = email_receiver
    msg["Cc"] = cc_receiver

    receivers_list = [email_receiver, cc_receiver]
    html = html_body
    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(
            email_sender, receivers_list, msg.as_string()
        )
