import httpx
from .base import NotificationAdapter

class TelegramAdapter(NotificationAdapter):
    def __init__(self, bot_token: str):
        self.bot_token = bot_token
        self.api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    async def send(self, recipient: str, message: str):
        """
        recipient: Telegram chat ID (string or numeric ID)
        message: Text message to send
        """
        payload = {
            "chat_id": recipient,
            "text": message,
            "parse_mode": "Markdown"  # or "HTML"
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.api_url, json=payload)
                response.raise_for_status()
                print(f"[Telegram] Sent to {recipient}")
        except httpx.HTTPStatusError as e:
            print(f"[Telegram] Failed: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"[Telegram] Error: {str(e)}")