from fastapi import FastAPI, HTTPException
from notifier import Notifier
from models import NotificationRequest
from template_renderer import render_notification

from adapters.email_adapter import EmailAdapter
from adapters.slack_adapter import SlackAdapter
from adapters.telegram_adapter import TelegramAdapter
from adapters.sms_adapter import SMSAdapter

import os

app = FastAPI()
notifier = Notifier()

SMTP_CONFIG = {
    "smtp_host": os.getenv("SMTP_HOST", "smtp.gmail.com"),
    "smtp_port": int(os.getenv("SMTP_PORT", 465)),
    "smtp_user": os.getenv("SMTP_USER", "rskirong@gmail.com"),
    "smtp_pass": os.getenv("SMTP_PASS", "")
}

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

sms_adapter = SMSAdapter(
    account_sid=os.getenv("TWILIO_ACCOUNT_SID", ""),
    auth_token=os.getenv("TWILIO_AUTH_TOKEN", ""),
    from_number=os.getenv("TWILIO_PHONE_NUMBER", "")
)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

# Register adapters
notifier.register_adapter("email", EmailAdapter(**SMTP_CONFIG))
notifier.register_adapter("slack", SlackAdapter(webhook_url=SLACK_WEBHOOK_URL))
notifier.register_adapter("telegram", TelegramAdapter(bot_token=TELEGRAM_BOT_TOKEN))
notifier.register_adapter("sms", sms_adapter)

@app.post("/notify")
async def send_notification(request: NotificationRequest):
    try:
        rendered_message = render_notification(
            channel=request.channel,
            recipient=request.recipient,
            message=request.message
        )
        await notifier.notify(request.channel, request.recipient, rendered_message)
        return {"status": "sent", "channel": request.channel}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))