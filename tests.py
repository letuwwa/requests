from random import randint
from framework.tools.data_parser import DataParser
from framework.tools.json_reader import JsonReader
from framework.exceptions.custom_exceptions import ResponseCodes


def test_connection_response(actions):
    base_url = JsonReader('config.json').get_url()
    response = actions.get_request_to_page(link=base_url)
    assert response.status_code == ResponseCodes.ok_code.value


def test_search_page_response(actions):
    response = actions.search_by_key_word('python')
    assert response.status_code == ResponseCodes.ok_code.value


def test_search_without_result(actions):
    parser = DataParser()
    key_word = 'shotgun'

    no_result = "По запросу «" + key_word + "» ничего не найдено"

    response = actions.search_by_key_word(key_word)
    is_string_exists = parser.is_string_exist_in_source(string=no_result, source=response.text)
    assert is_string_exists is True


def test_average_key_words(actions):
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

    assert linux_average - 10 <= linux_words_on_random_page <= linux_average + 10
    assert python_average - 10 <= python_words_on_random_page <= python_average + 10
    assert flask_average - 10 <= flask_words_on_random_page <= flask_average + 10


def test_response_url(actions):
    response = actions.get_request_to_page(actions.base_url)
    assert actions.base_url + '/' == response.url


def test_response_encoding(actions):
    encoding = 'utf-8'
    response = actions.get_request_to_page(actions.base_url)
    assert encoding == response.encoding


def test_is_page_redirect(actions):
    response = actions.get_request_to_page(actions.base_url)
    assert response.is_redirect is False
