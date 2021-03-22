import re


class DataParser:
    @classmethod
    def get_links_to_vacancies(cls, source):
        """
            Method that parses all vacancies links from page source
        :param source:
            a page source
        :return:
            a list of links
        """
        return re.findall(r'https://rabota.by/vacancy/\d+', source)

    @classmethod
    def is_string_exist_in_source(cls, string, source):
        """
            Method that check if string exist in source
        :param string:
            string to find
        :param source:
            data source
        :return:
            True - if string exists
            False - if string doesn't exist
        """
        result = re.findall(string, source)
        if result:
            return True
        else:
            return False

    @classmethod
    def count_key_words_on_source(cls, key_word, source):
        """
            Method that count key words in source
        :param key_word:
            key word to find
        :param source:
            data source
        :return:
            number of words found
        """
        return len(re.findall('[' + key_word[0].upper() + '.' + key_word[0].lower() + ']' + key_word[1:], source))
