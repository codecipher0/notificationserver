from .base import NotificationAdapter

class SMSAdapter(NotificationAdapter):
    def send(self, recipient: str, message: str):
        print(f"[SMS] To: {recipient} | Message: {message}")
        # Actual implementation would use Twilio or another SMS API