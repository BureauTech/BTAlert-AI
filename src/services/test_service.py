from prometheus_api_client import PrometheusConnect

from config import _ENV


prom = PrometheusConnect(url=f'http://{_ENV["PROMETHEUS_HOST"]}:9090', disable_ssl=True)
