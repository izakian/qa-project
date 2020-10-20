from googlesearch import search as gsearch
import urllib.request
from bs4 import BeautifulSoup

class GoogleSearch:

    @staticmethod
    def _get_url(input_text, result_num):
        """search input_text and return  result_num pages

        Args:
            input_text (str): [description]
            result_num (int, optional): [description]. Defaults to cls.result_num.
        """

        urls = []
        for url in gsearch(query=input_text,
                           num=result_num,
                           stop=result_num,
                           tld="co.in",
                           lang='en',
                           start=0,
                           pause=2.0):
            urls.append(url)
        return urls

    @staticmethod
    def _extract_text(urls):
        texts = []
        for url in urls:
            html = urllib.request.urlopen(url).read()
            text = BeautifulSoup(html).text.replace("\n", ".")
            texts.append(text)
        return texts

    @classmethod
    def run(cls, input_text, result_num):
            return cls._extract_text(cls._get_url(input_text, result_num))
