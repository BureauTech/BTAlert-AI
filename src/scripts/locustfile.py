from time import time
from random import randint, random

from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    wait_time = between(1, 5)

    def on_start(self) -> None:
        json = {'useEmail': 'admin@bureautech.com', 'usePassword': 'admin'}
        self.client.post('/login', json=json)

    def on_stop(self) -> None:
        self.client.get('/logout')

    @staticmethod
    def random_user() -> dict:
        return {
            'useName': f'user-{time()}-{random()}',
            'useEmail': f'user-{time()}-{random()}@bureautech.com',
            'usePhone': f'{time()}-{random()}',
            'usePassword': f'{time()}-{random()}'
        }

    @task(2)
    def create_user(self) -> dict:
        cookies = self.client.cookies.get_dict()
        response = self.client.post('/user', json=self.random_user(), cookies=cookies)
        if response.status_code != 200:
            return None
        return response.json()

    @task(3)
    def get_user(self) -> dict:
        user = self.create_user()
        if user is None:
            return None
        use_cod = user['data']['useCod']
        cookies = self.client.cookies.get_dict()
        response = self.client.get(f'/user/{use_cod}', cookies=cookies)
        if response.status_code != 200:
            return None
        return response.json()

    @task(3)
    def get_users(self) -> dict:
        params = {'page': randint(0, 100)}
        cookies = self.client.cookies.get_dict()
        response = self.client.get('/user', params=params, cookies=cookies)
        if response.status_code != 200:
            return None
        return response.json()

    @task(2)
    def update_user(self) -> dict:
        user = self.create_user()
        if user is None:
            return None
        use_cod = user['data']['useCod']
        cookies = self.client.cookies.get_dict()
        response = self.client.put(f'/user/{use_cod}', json=self.random_user(), cookies=cookies)
        if response.status_code != 200:
            return None
        return response.json()

    @task(1)
    def delete_user(self) -> dict:
        user = self.create_user()
        if user is None:
            return None
        use_cod = user['data']['useCod']
        cookies = self.client.cookies.get_dict()
        response = self.client.delete(f'/user/{use_cod}', cookies=cookies)
        if response.status_code != 200:
            return None
        return response.json()
