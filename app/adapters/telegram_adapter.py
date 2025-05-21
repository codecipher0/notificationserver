from .base import NotificationAdapter

class TelegramAdapter(NotificationAdapter):
    def send(self, recipient: str, message: str):
        print(f"[Telegram] To: {recipient} | Message: {message}")
        # Actual implementation would use Telegram Bot API