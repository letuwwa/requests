import pytest
from framework.exceptions.custom_exceptions import ResponseCodes, IncorrectStatusCodeError
from framework.requests_tool import RequestsTool
from framework.tools.json_reader import JsonReader


@pytest.fixture()
def actions():
    base_url = JsonReader('config.json').get_url()
    actions = RequestsTool(base_url=base_url)
    response = actions.get_request_to_page(link=base_url)
    if response.status_code == ResponseCodes.ok_code.value:
        yield actions
    else:
        raise IncorrectStatusCodeError()
