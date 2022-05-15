import os

from prometheus_client import generate_latest
from prometheus_api_client import PrometheusConnect

from metrics.config import Metric


class Collector:

    def __init__(self) -> None:
        self.prom = PrometheusConnect(os.getenv('PROMETHEUS_URL'), disable_ssl=True)

    def get_metrics(self) -> bytes:
        Metric.BTALERT_INFO.info({'version': 'v1.0.0'})

        requests_per_second = None
        data = self.prom.get_current_metric_value(
            '(idelta(nginx_vts_server_requests_total{code="total", host="*"}[1m]) - 1) / 15'
        )
        if data:
            requests_per_second = round(float(data[0]['value'][1]), 2)
            Metric.BTALERT_REQUESTS_PER_SECOND.set(requests_per_second)

        failed_requests_percent = None
        data = self.prom.get_current_metric_value(
            'sum(idelta(nginx_vts_server_requests_total{code=~"4xx|5xx", host="*"}[1m])) / 15'
        )
        if data and requests_per_second:
            failed_requests_percent = round(float(data[0]['value'][1]) / requests_per_second * 100, 2)
            Metric.BTALERT_FAILED_REQUESTS_PERCENT.set(min(100, failed_requests_percent))

        return generate_latest()
