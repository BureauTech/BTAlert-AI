import os
import warnings
from datetime import datetime, timedelta
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
from prometheus_api_client import MetricSnapshotDataFrame, PrometheusConnect
from prometheus_api_client.utils import parse_datetime
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 1.5


warnings.filterwarnings('ignore')


load_dotenv()


class BtalertIA:
    def __init__(self, last_minutes_importance: int, regressor=None) -> None:
        """
        Args:
            last_minutes_importance (int): The last minutes that matter to foreacasting (context)
        """
        self.prom = PrometheusConnect(
            url=os.getenv('PROMETHEUS_URL'), disable_ssl=True)
        self.regressor = regressor
        if regressor is None:
            self.regressor = RandomForestRegressor(
                max_depth=40,
                n_estimators=3,
                random_state=123,
            )
        self.forecaster = ForecasterAutoreg(
            regressor=self.regressor,
            lags=self.minutes_to_step(last_minutes_importance)
        )
        self.original_dataframe = pd.DataFrame()
        self.data_train = pd.DataFrame()
        self.data_test = pd.DataFrame()
        self.predictions = pd.Series()
        self.value_column = 'value'
        self.timestamp_column = 'timestamp'

    def load_metric_as_dataframe(self, start: str, end: str, metric_name: str) -> pd.DataFrame:
        start_time = parse_datetime(start)
        end_time = parse_datetime(end)
        original_dataframe = MetricSnapshotDataFrame(
            self.prom.get_metric_range_data(
                metric_name, start_time=start_time, end_time=end_time, chunk_size=timedelta(seconds=15))
        )

        new_dataframe = original_dataframe[[
            self.timestamp_column, self.value_column]].copy()
        new_dataframe[self.timestamp_column] = [datetime.fromtimestamp(
            timestamp) for timestamp in new_dataframe[self.timestamp_column]]
        new_dataframe[self.value_column] = [
            float(value) for value in new_dataframe[self.value_column]]

        new_dataframe[self.timestamp_column] = new_dataframe[self.timestamp_column].astype(
            'datetime64[s]')
        new_dataframe = new_dataframe.set_index(
            new_dataframe[self.timestamp_column])

        new_dataframe = new_dataframe.asfreq(freq='15S', method='bfill')
        self.original_dataframe = new_dataframe
        return new_dataframe

    def split_test_train_dataframe(self, minutes_split: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        steps = self.minutes_to_step(minutes_split)

        self.data_train = self.original_dataframe[:-steps]
        self.data_test = self.original_dataframe[-steps:]

        return self.data_train, self.data_test

    def minutes_to_step(self, min: int) -> int:
        return int((min * 60) / 15)

    def train_model(self) -> None:
        self.forecaster.fit(y=self.data_train[self.value_label])

    def predict(self, minutes_prediction: int) -> pd.Series:
        return self.forecaster.predict(steps=self.minutes_to_step(minutes_prediction))

    def plot_graphic(self):
        fig, ax = plt.subplots(figsize=(18, 12))
        self.data_train[self.value_column].plot(ax=ax, label='train')
        self.data_test[self.value_column].plot(ax=ax, label='test')
        self.predictions.plot(ax=ax, label='predictions')
        ax.legend()

    def get_mean_squared_error(self) -> float:
        error_mse: float = mean_squared_error(
            y_true=self.data_test[self.value_column],
            y_pred=self.predictions
        )
        return error_mse

    def execute(self, start: str, end: str, metric_name: str, minutes_split: int):
        self.load_metric_as_dataframe(start, end, metric_name)
        self.split_test_train_dataframe(minutes_split)
        self.train_model()
        self.predict()
