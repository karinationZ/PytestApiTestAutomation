from clients.base_client import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class DemoClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URI
        self.request = APIRequest()

    def get_users(self):
        return self.request.get(f'{BASE_URI}/users')
