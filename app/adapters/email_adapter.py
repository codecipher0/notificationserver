#pip install aiosmtplib email-validator
from aiosmtplib import SMTP
from email.message import EmailMessage
from .base import NotificationAdapter

#SMTP_HOST = "smtp.gmail.com"
#SMTP_PORT = 587
#SMTP_USER = "rskirong@gmail.com"
#SMTP_PASS = "" 

class EmailAdapter(NotificationAdapter):
    def __init__(self, smtp_host: str, smtp_port: int, smtp_user: str, smtp_pass: str):
            self.smtp_host = smtp_host
            self.smtp_port = smtp_port
            self.smtp_user = smtp_user
            self.smtp_pass = smtp_pass
            
    async def send(self, recipient: str, message: str):
        email = EmailMessage()
        email["From"] = self.smtp_user
        email["To"] = recipient
        email["Subject"] = "Notification"
        email.set_content(message)

        try:
            smtp = SMTP(hostname=self.smtp_host, port=self.smtp_port, use_tls=True)
            await smtp.connect()
            #await smtp.starttls()
            await smtp.login(self.smtp_user, self.smtp_pass)
            await smtp.send_message(email)
            await smtp.quit()
            print(f"[Email] Sent to {recipient}")
        except Exception as e:
            print(f"[Email] Failed to send to {recipient}: {e}")