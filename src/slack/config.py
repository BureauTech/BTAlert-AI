class AlertTemplate:

    @staticmethod
    def get_dict() -> dict:
        return {
            'text': 'Para de ler, Denis, seu vagabundo kkk',
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Type:*\nComputer (laptop)"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*When:*\nSubmitted Aut 10"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Reason:*\nAll vowel keys aren't working."
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
                        }
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "emoji": True,
                                "text": "Approve"
                            },
                            "style": "primary",
                            "value": "click_me_123"
                        },
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "emoji": True,
                                "text": "Deny"
                            },
                            "style": "danger",
                            "value": "click_me_123"
                        }
                    ]
                }
            ]
        }
