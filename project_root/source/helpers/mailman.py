"""
    A Module to send emails
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from . import app, config


def __make_mail_body(mail_type, data=None):
    if data is None:
        data = {}
    text = config.EMAIL_BODY[mail_type]
    if mail_type == 'reset' and data:
        text = text.format(**data)

    part1 = MIMEText(text, 'plain')
    msg = MIMEMultipart('alternative')
    msg.attach(part1)
    return msg


def __send_mail(mail_type, receivers, body_data=None, error_bubble_up=False):
    if body_data is None:
        body_data = {}
    try:
        msg = __make_mail_body(mail_type, body_data)
        server = config.EMAIL_SERVER_HOST
        port = config.SMTP_EMAIL_SERVER_PORT
        user = config.EMAIL_SERVER_USER
        password = config.EMAIL_SERVER_USER_PASSWORD
        sender = config.EMAIL_SENDER_NAME

        msg['Subject'] = config.EMAIL_HEADER[mail_type]
        msg['From'] = config.EMAIL_SENDER_NAME
        msg['To'] = ", ".join(receivers)

        mail = smtplib.SMTP(server, port)
        mail.starttls()
        mail.login(user, password)
        mail.sendmail(sender, receivers, msg.as_string())
        mail.quit()
    except Exception as e:
        if error_bubble_up or config.DEBUG:
            raise
        app.logger.error("Mail not send to %s. %s", receivers, e)


def send_mail(receiver: list, data: dict, error_bubble_up=False):
    """
        Send Emails
        Preferable to call this function asynchronously

        :params:
         * receiver: list of receivers
         * data: A dictionary to put data in to body; make sure same variables are used in config
         * error_bubble_up: Flag to decide where to handle variable or not

        :returns:
        none
    """
    receiver = [receiver] if type(receiver) is str else receiver
    __send_mail(
        mail_type='reset',
        receivers=receiver,
        body_data=data,
        error_bubble_up=error_bubble_up
    )
