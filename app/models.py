from pydantic import BaseModel

class NotificationRequest(BaseModel):
    channel: str
    recipient: str
    message: str