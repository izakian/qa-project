from flask import Flask, jsonify
from qa_model import WikiSearch, QAModel

app = Flask(__name__)

@app.route('/')
def health_ckeck():
    return "Ok!"

@app.route('/<question>')
def hello_name(question):
    texts = WikiSearch.search(question)
    answers = QAModel.predict(question, texts)
    d = {}
    for i in range(len(answers)):
        d[i] = answers[i]
    return jsonify(d)

if __name__ == '__main__':
    app.run()