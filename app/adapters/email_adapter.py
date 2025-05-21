from .base import NotificationAdapter

class EmailAdapter(NotificationAdapter):
    def send(self, recipient: str, message: str):
        print(f"[Email] To: {recipient} | Message: {message}")
        # Actual implementation would use smtplib or an email API