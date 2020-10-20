from code import GoogleSearch, QAModel

question = "who is donald trump?"
num_results = 3

texts = GoogleSearch.run(question, num_results)
answers = QAModel.predict(question, texts)
for answer in answers:
    print(answer)
    print("==="*10)