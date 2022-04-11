import os

from flask import Flask
from dotenv import load_dotenv
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Gauge
from prometheus_api_client import PrometheusConnect


load_dotenv()


app = Flask(__name__)
prom = PrometheusConnect(url=os.getenv('PROMETHEUS_URL'), disable_ssl=True)

btalert_ai_prediction = Gauge('btalert_ai_prediction', 'estimated time in hours for the system to be down')
btalert_ai_prediction.set(1)

btalert_ai_total_metrics = Gauge('btalert_ai_total_metrics', 'total of metrics available on promethus')
btalert_ai_total_metrics.set(len(prom.all_metrics()))

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    app.run('localhost', 5050)
