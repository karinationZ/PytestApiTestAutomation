import pytest
from clients.DemoClient import DemoClient


@pytest.fixture(scope='module')
def demo_client():
    yield DemoClient()
