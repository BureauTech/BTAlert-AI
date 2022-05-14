import os
from base64 import b64decode

from slack_sdk.webhook import WebhookClient
from slack.config import AlertTemplate


class Messenger:

    def __init__(self) -> None:
        self.webhook = WebhookClient(
            b64decode(os.getenv('SLACK_TOKEN')).decode().strip()
        )

    def send_alert(self) -> None:
        self.webhook.send_dict(AlertTemplate.get_dict())
