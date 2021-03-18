from framework.requests_tool import RequestsTool


def test_one():
    actions = RequestsTool()
    links_list = []
    page_count = 3

    for i in range(page_count):
        response = actions.search_by_key_word('python', page_number=i)
        page_links = actions.get_links_to_vacancies(response.text)
        links_list.extend(page_links)

    links_count = len(links_list)
    linux_words = 0
    python_words = 0
    flask_words = 0

    for link in links_list:
        page_data = actions.get_page_data(link)
        linux_words += actions.count_key_words_on_page(text=page_data, key_word='linux')
        python_words += actions.count_key_words_on_page(text=page_data, key_word='python')
        flask_words += actions.count_key_words_on_page(text=page_data, key_word='flask')

    print('all links - ', links_count)
    print('all linux words - ', linux_words, '\n\taverage - ', round(linux_words/links_count))
    print('all python words - ', python_words, '\n\taverage - ', round(python_words/links_count))
    print('all flask words - ', flask_words, '\n\taverage - ', round(flask_words/links_count))
