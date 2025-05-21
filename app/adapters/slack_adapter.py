from .base import NotificationAdapter

class SlackAdapter(NotificationAdapter):
    def send(self, recipient: str, message: str):
        print(f"[Slack] Channel/User: {recipient} | Message: {message}")
        # Actual implementation would use Slack API