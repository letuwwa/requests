import requests


class RequestsTool:
    def __init__(self):
        self.headers = {"User-Agent": "Chrome/89.0.4389.90"}

        self.base_url = 'http://jobs.tut.by'
        self.search_url_addon = '/search/vacancy?area=1002&fromSearchLine=true&st=searchVacancy&text='


    def search_by_key_word(self, key_word):
        return requests.get(self.base_url + self.search_url_addon + key_word, headers=self.headers)
