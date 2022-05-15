from slack.alerts.alert import Alert


class WarningAlert(Alert):

    def get_dict(self) -> dict:
        return {
            'blocks': [
                {
                    'type': 'header',
                    'text': {
                        'type': 'plain_text',
                        'text': '⚠️ [WARNING ALERT - 1239] ⚠️'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': 'You are receiving this warning because our ' 
                                'artificial intelligence system has detected ' 
                                'a possible unavailability in your application.'
                    }
                },
                {
                    'type': 'divider'
                },
                {
                    'type': 'section',
                    'fields': [
                        {
                            'type': 'mrkdwn',
                            'text': '📅 *When:*\n16/05/2022 12:41:23'
                        }
                    ]
                }
            ]
        }
