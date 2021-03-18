import requests
import re


class RequestsTool:
    def __init__(self):
        self.headers = {"User-Agent": "Chrome/89.0.4389.90"}

        self.base_url = 'https://rabota.by'
        self.search_url_addon = '/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text='
        self.page_addon = '&page='
        self.key_word = None

    def search_by_key_word(self, key_word, page_number=None):
        self.key_word = key_word
        if page_number is None:
            return requests.get(self.base_url + self.search_url_addon + self.key_word, headers=self.headers)
        else:
            return requests.get(self.base_url + self.search_url_addon + self.key_word +
                                self.page_addon + str(page_number - 1), headers=self.headers)

    def get_links_to_vacancies(self, text):
        return re.findall(self.base_url + r'/vacancy/\d+', text)

    def get_page_data(self, link):
        return requests.get(link, headers=self.headers).text

    @classmethod
    def count_key_words_on_page(cls, text, key_word):
        return len(re.findall('[' + key_word[0].upper() + '.' + key_word[0].lower() + ']' + key_word[1:], text))
