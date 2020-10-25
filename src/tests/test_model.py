import unittest
from src.model import QAModel

class TestQAModel(unittest.TestCase):

    question = "Who is Donald Trump"
    texts = ["Donlad Trump is the 45th president of the united states of America",
              "Donald Trump is the son of Senior Trump", 
              "Donald Trump is a US citizen"]
    def setUp(self):
        self.answers = QAModel.predict(question=self.question, texts=self.texts)

    def test_answer_size(self):
        self.assertEqual(len(self.answers), 3)