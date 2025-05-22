#pip install httpx

import httpx
from .base import NotificationAdapter

class SlackAdapter(NotificationAdapter):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    async def send(self, recipient: str, message: str):
        """
        recipient: Slack channel (e.g., '#general') or @username for DM
        message: Rendered message to post
        """
        payload = {
            "text": message,
            "channel": recipient  # optional: depends on webhook permissions
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.webhook_url, json=payload)
                response.raise_for_status()
                print(f"[Slack] Sent to {recipient}")
        except httpx.HTTPStatusError as e:
            print(f"[Slack] Failed: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"[Slack] Error: {str(e)}")