import re
import wikipedia

class WikiSearch:

    @staticmethod
    def _extract_text(question, num_results):
        wiki_page =  wikipedia.search(question, results=num_results)
        texts = []
        for page in wiki_page:
            text = wikipedia.summary(page)
            texts.append(text[0:512])
        return texts

    @classmethod
    def search(cls, question, result_num=3):
            return cls._extract_text(question, result_num)
