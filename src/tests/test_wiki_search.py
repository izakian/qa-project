import unittest
from src.wiki_search import WikiSearch

class TestWikiSearch(unittest.TestCase):

    texts = []
    question = "Donald Trump"
    result_num = 5

    def setUp(self):
        self.texts = WikiSearch.search(question=self.question, result_num=self.result_num)

    def test_text_size(self):
        self.assertEqual(len(self.texts), self.result_num)
    
    def text_lengh(self):
        self.assertTrue(all([len(text)<=512 for text in texts]))
