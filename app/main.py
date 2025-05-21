from fastapi import FastAPI, HTTPException
from notifier import Notifier
from models import NotificationRequest

from adapters.email_adapter import EmailAdapter
from adapters.slack_adapter import SlackAdapter
from adapters.telegram_adapter import TelegramAdapter
from adapters.sms_adapter import SMSAdapter

app = FastAPI()
notifier = Notifier()

# Register adapters
notifier.register_adapter("email", EmailAdapter())
notifier.register_adapter("slack", SlackAdapter())
notifier.register_adapter("telegram", TelegramAdapter())
notifier.register_adapter("sms", SMSAdapter())

@app.post("/notify")
def send_notification(request: NotificationRequest):
    try:
        notifier.notify(request.channel, request.recipient, request.message)
        return {"status": "sent", "channel": request.channel}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))