import os

from dotenv import load_dotenv
from prometheus_client import generate_latest
from prometheus_api_client import PrometheusConnect

from metrics.config import Config


load_dotenv()


class Collector:

    def __init__(self) -> None:
        self.prom = PrometheusConnect(url=os.getenv('PROMETHEUS_URL'), disable_ssl=True)

    def __update_metrics(self) -> None:
        requests_per_second = round(float(self.prom.get_current_metric_value(
            '(idelta(nginx_vts_server_requests_total{code="total", host="*"}[1m]) - 1) / 15',
        )[0]['value'][1]), 2)

        if not requests_per_second:
            failed_requests_percent = 0
        else:
            failed_requests_percent = round(float(self.prom.get_current_metric_value(
                'sum(idelta(nginx_vts_server_requests_total{code=~"4xx|5xx", host="*"}[1m])) / 15'
            )[0]['value'][1]), 2) / requests_per_second * 100

        Config.BTALERT_REQUESTS_PER_SECOND.set(requests_per_second)
        Config.BTALERT_FAILED_REQUESTS_PERCENT.set(failed_requests_percent)

    def get_metrics(self) -> bytes:
        self.__update_metrics()
        return generate_latest()
