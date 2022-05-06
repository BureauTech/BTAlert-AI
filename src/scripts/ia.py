import os
from prometheus_client import Gauge
from prometheus_api_client import PrometheusConnect, MetricSnapshotDataFrame
from prometheus_api_client.utils import parse_datetime
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 1.5

load_dotenv()
from skforecast.ForecasterAutoreg import ForecasterAutoreg
ForecasterAutoreg().fit
prom = PrometheusConnect(url=os.getenv('PROMETHEUS_URL'), disable_ssl=True)

start_time = parse_datetime("12h")
end_time = parse_datetime("now")

requests_seconds = MetricSnapshotDataFrame(prom.get_metric_range_data('nginx_vts_server_request_seconds', start_time=start_time, end_time=end_time, label_config={'host': '172.16.2.108'}, chunk_size=timedelta(seconds=15)))


req_dataframe = requests_seconds[['timestamp', 'value']].copy()
req_dataframe['timestamp'] = [datetime.fromtimestamp(timestamp) for timestamp in req_dataframe['timestamp']]
req_dataframe['value'] = [float(value) for value in req_dataframe['value']]

req_dataframe = req_dataframe.set_index('timestamp')

#print(req_dataframe.head())

steps = 36
data_train = req_dataframe[:-steps]
data_test  = req_dataframe[-steps:]

print(f"Train dates : {data_train.index.min()} --- {data_train.index.max()}  (n={len(data_train)})")
print(f"Test dates  : {data_test.index.min()} --- {data_test.index.max()}  (n={len(data_test)})")

fig, ax=plt.subplots(figsize=(9, 4))
data_train['value'].plot(ax=ax, label='train')
data_test['value'].plot(ax=ax, label='test')
ax.legend()