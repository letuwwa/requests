from framework.tools.data_parser import DataParser
from framework.requests_tool import RequestsTool
from framework.tools.json_reader import JsonReader


def test_connection():
    pass


def test_one():
    base_url = JsonReader('config.json').get_url()

    actions = RequestsTool(base_url=base_url)
    parser = DataParser(base_url=base_url)

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
        linux_words += parser.count_key_words_on_page(text=page_data, key_word='linux')
        python_words += parser.count_key_words_on_page(text=page_data, key_word='python')
        flask_words += parser.count_key_words_on_page(text=page_data, key_word='flask')

    print('all links - ', links_count)
    print('all linux words - ', linux_words, '\n\taverage - ', round(linux_words/links_count))
    print('all python words - ', python_words, '\n\taverage - ', round(python_words/links_count))
    print('all flask words - ', flask_words, '\n\taverage - ', round(flask_words/links_count))
