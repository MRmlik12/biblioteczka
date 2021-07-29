"""Email service"""
import smtplib
from email.mime.text import MIMEText

from catana.core.config import EMAIL, EMAIL_HOST, EMAIL_PASSWORD, EMIAL_HOST_PORT


class Email:
    """Class to send emails to users"""

    smtp: smtplib.SMTP

    def __init__(self):
        """Connect to SMTP server"""
        self.smtp = smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMIAL_HOST_PORT)
        self.smtp.ehlo()
        self.smtp.login(EMAIL, EMAIL_PASSWORD)

    def send(self, email: str, user_email: str, subject: str, content: str):
        """Send example email"""
        msg = MIMEText(content)
        msg["Subject"] = subject
        msg["From"] = email
        msg["To"] = user_email
        self.smtp.send_message(msg)

    def close_connection(self):
        """Close connection"""
        self.smtp.close()
