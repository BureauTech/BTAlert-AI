from dotenv import load_dotenv
from flask import Flask, Response

from metrics.collector import Collector
# from slack.messenger import Messenger
# from slack.alerts.info_alert import InfoAlert
# from slack.alerts.warning_alert import WarningAlert


load_dotenv()

# messenger = Messenger()
# print(
#     messenger.send_alert(WarningAlert())
# )


app = Flask(__name__)
collector = Collector()

@app.route('/metrics')
def get_metrics():
    return Response(collector.get_metrics(), mimetype='text/plain')

if __name__ == '__main__':
    app.run('localhost', 5050)
