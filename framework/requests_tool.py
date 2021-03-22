import requests


class RequestsTool:
    def __init__(self, base_url=None):
        self.headers = {"User-Agent": "Chrome/89.0.4389.90"}

        self.base_url = base_url
        self.search_url_addon = '/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text='
        self.page_addon = '&page='
        self.key_word = None

    def search_by_key_word(self, key_word, page_number=None):
        self.key_word = key_word
        if page_number is None:
            response = requests.get(self.base_url + self.search_url_addon + self.key_word, headers=self.headers)
        else:
            response = requests.get(self.base_url + self.search_url_addon + self.key_word +
                                    self.page_addon + str(page_number - 1), headers=self.headers)
        return response

    def get_request_to_page(self, link):
        return requests.get(link, headers=self.headers)
