import httpx
from .base import NotificationAdapter
import base64

class SMSAdapter(NotificationAdapter):
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        self.base_url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"

        # Basic Auth header (for httpx)
        auth_string = f"{account_sid}:{auth_token}"
        self.auth_header = {
            "Authorization": "Basic " + base64.b64encode(auth_string.encode()).decode()
        }

    async def send(self, recipient: str, message: str):
        payload = {
            "To": recipient,
            "From": self.from_number,
            "Body": message,
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.base_url, data=payload, headers=self.auth_header)
                response.raise_for_status()
                print(f"[SMS] Sent to {recipient}")
        except httpx.HTTPStatusError as e:
            print(f"[SMS] Failed: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"[SMS] Error: {str(e)}")