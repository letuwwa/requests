from random import randint
from framework.tools.data_parser import DataParser
from framework.requests_tool import RequestsTool
from framework.tools.json_reader import JsonReader
from framework.exceptions.custom_exceptions import ResponseCodes


def test_connection_response():
    base_url = JsonReader('config.json').get_url()
    actions = RequestsTool(base_url=base_url)

    response = actions.get_request_to_page(link=base_url)
    assert response.status_code == ResponseCodes.ok_code.value


def test_search_page_response():
    base_url = JsonReader('config.json').get_url()
    action = RequestsTool(base_url=base_url)

    response = action.search_by_key_word('python')
    assert response.status_code == ResponseCodes.ok_code.value


def test_search_without_result():
    base_url = JsonReader('config.json').get_url()
    action = RequestsTool(base_url=base_url)
    parser = DataParser()

    no_result = "По запросу «shotgun» ничего не найдено"

    response = action.search_by_key_word('shotgun')
    is_string_exists = parser.is_string_exist_in_source(string=no_result, source=response.text)
    assert is_string_exists is True


def test_average_key_words():
    base_url = JsonReader('config.json').get_url()
    actions = RequestsTool(base_url=base_url)
    parser = DataParser()

    links_list = []
    page_count = 1

    for i in range(page_count):
        response = actions.search_by_key_word('python', page_number=i)
        page_links = parser.get_links_to_vacancies(response.text)
        links_list.extend(page_links)

    links_count = len(links_list)
    linux_words = 0
    python_words = 0
    flask_words = 0

    for link in links_list:
        page_data = actions.get_request_to_page(link).text
        linux_words += parser.count_key_words_on_source(source=page_data, key_word='linux')
        python_words += parser.count_key_words_on_source(source=page_data, key_word='python')
        flask_words += parser.count_key_words_on_source(source=page_data, key_word='flask')

    linux_average = round(linux_words / links_count)
    python_average = round(python_words / links_count)
    flask_average = round(flask_words / links_count)

    random_page_data = actions.get_request_to_page(link=links_list[randint(0, links_count - 1)]).text
    linux_words_on_random_page = parser.count_key_words_on_source(source=random_page_data, key_word='linux')
    python_words_on_random_page = parser.count_key_words_on_source(source=random_page_data, key_word='python')
    flask_words_on_random_page = parser.count_key_words_on_source(source=random_page_data, key_word='flask')

    assert linux_average - 1 <= linux_words_on_random_page <= linux_average + 1
    assert python_average - 1 <= python_words_on_random_page <= python_average + 1
    assert flask_average - 1 <= flask_words_on_random_page <= flask_average + 1

    print('all links - ', links_count)
    print('all linux words - ', linux_words, '\n\taverage - ', round(linux_words / links_count))
    print('all python words - ', python_words, '\n\taverage - ', round(python_words / links_count))
    print('all flask words - ', flask_words, '\n\taverage - ', round(flask_words / links_count))
