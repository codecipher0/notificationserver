from typing import Dict
from adapters.base import NotificationAdapter

class Notifier:
    def __init__(self):
        self.adapters: Dict[str, NotificationAdapter] = {}

    def register_adapter(self, name: str, adapter: NotificationAdapter):
        self.adapters[name] = adapter

    def notify(self, channel: str, recipient: str, message: str):
        if channel not in self.adapters:
            raise ValueError(f"No adapter registered for channel '{channel}'")
        self.adapters[channel].send(recipient, message)