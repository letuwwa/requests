import re


class DataParser:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_links_to_vacancies(self, text):
        return re.findall(self.base_url + r'/vacancy/\d+', text)

    @classmethod
    def count_key_words_on_page(cls, text, key_word):
        return len(re.findall('[' + key_word[0].upper() + '.' + key_word[0].lower() + ']' + key_word[1:], text))