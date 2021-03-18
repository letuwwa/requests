from framework.requests_tool import RequestsTool


def test_one():
    actions = RequestsTool()
    links_list = []
    page_count = 5

    for i in range(page_count):
        response = actions.search_by_key_word('python', page_number=i)
        page_links = actions.get_links_to_vacancies(response.text)
        links_list.extend(page_links)

    for link in links_list:
        print(link)
    print(len(links_list))
