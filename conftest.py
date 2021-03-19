import pytest
from framework.tools.json_reader import JsonReader


@pytest.fixture
def config():
    json_reader = JsonReader('config.json')
    return json_reader
