import os
from base64 import b64decode

from slack_sdk.webhook import WebhookClient
from slack_sdk.webhook.webhook_response import WebhookResponse

from slack.alerts.alert import Alert


class Messenger:

    def __init__(self) -> None:
        self.webhook = WebhookClient(
            b64decode(os.getenv('SLACK_TOKEN')).decode().strip()
        )

    def send_alert(self, alert: Alert) -> WebhookResponse:
        return self.webhook.send_dict(alert.get_dict())
