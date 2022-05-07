from prometheus_client import Gauge


class Config:

    BTALERT_REQUESTS_PER_SECOND = \
        Gauge('btalert_requests_per_second', 'Requests per second sent to nginx')

    BTALERT_FAILED_REQUESTS_PERCENT = \
        Gauge('btalert_failed_requests_percent', 'Percentage of failed requests sent to nginx')
