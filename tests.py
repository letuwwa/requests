from framework.requests_tool import RequestsTool


def test_one():
    actions = RequestsTool()
    result = actions.search_by_key_word('python')
    print(result.text)
