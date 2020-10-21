from code import WikiSearch, QAModel

question = "who is barak obama?"

texts = WikiSearch.run(question)
answers = QAModel.predict(question, texts)
for answer in answers:
    print(answer)
    print("==="*10)