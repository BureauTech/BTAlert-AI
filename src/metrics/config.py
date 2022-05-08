from prometheus_client import Gauge


class Metric:

    BTALERT_REQUESTS_PER_SECOND = Gauge(
        name='btalert_requests_per_second',
        documentation='Requests per second sent to nginx'
    )

    BTALERT_FAILED_REQUESTS_PERCENT = Gauge(
        name='btalert_failed_requests_percent',
        documentation='Percentage of failed requests sent to nginx'
    )
