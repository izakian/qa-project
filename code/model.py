from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

class QAModel:

    TOKENIZER = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
    MODEL= AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

    @classmethod
    def predict(cls, question, texts):
        answers = []
        for text in texts:
            inputs = cls.TOKENIZER.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
            input_ids = inputs["input_ids"].tolist()[0]
            text_tokens = cls.TOKENIZER.convert_ids_to_tokens(input_ids)
            answer_start_scores, answer_end_scores = cls.MODEL(**inputs)

            answer_start = torch.argmax(answer_start_scores) 
            answer_end = torch.argmax(answer_end_scores) + 1
            answer = cls.TOKENIZER.convert_tokens_to_string(cls.TOKENIZER.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
            answers.append(answer)
        return answers
