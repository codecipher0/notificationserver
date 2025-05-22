from typing import Dict
from adapters.base import NotificationAdapter

class Notifier:
    def __init__(self):
        self.adapters: Dict[str, NotificationAdapter] = {}

    def register_adapter(self, name: str, adapter: NotificationAdapter):
        self.adapters[name] = adapter

    async def notify(self, channel: str, recipient: str, message: str):
        adapter = self.adapters.get(channel)
        if not adapter:
            raise ValueError(f"No adapter registered for channel '{channel}'")
        await adapter.send(recipient, message)