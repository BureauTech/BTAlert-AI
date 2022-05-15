from typing_extensions import Self
from slack.alerts.alert import Alert


class InfoAlert(Alert):

    def get_dict(self) -> dict:
        return {
            'blocks': [
                {
                    'type': 'header',
                    'text': {
                        'type': 'plain_text',
                        'text': 'ℹ️ [INFO ALERT - 1424] ℹ️'
                    }
                }
            ]
        }
