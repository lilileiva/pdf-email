import os
import smtplib
from email.mime.text import MIMEText


class SMTPService:
    def __init__(
        self,
        host: str = os.getenv("MAILTRAP_HOST"),
        port: int = os.getenv("MAILTRAP_PORT"),
        user: str = os.getenv("MAILTRAP_USER"),
        password: str = os.getenv("MAILTRAP_PASSWORD"),
        sender_email: str = os.getenv("MAILTRAP_SENDER"),
        local_hostname: str = "localhost",
    ):
        self.client = smtplib.SMTP(host=host, port=port, local_hostname=local_hostname)
        self.client.starttls()
        self.client.login(user=user, password=password)
        self.sender_email = sender_email

    def send_email(self, receiver_email: str, subject: str, content: str) -> None:
        message = MIMEText(content, "plain")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = receiver_email
        self.client.sendmail(from_addr=self.sender_email, to_addrs=receiver_email, msg=message.as_string())
