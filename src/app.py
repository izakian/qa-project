from flask import Flask, jsonify
from model import QAModel
from wiki_search import WikiSearch

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def health_ckeck():
    return "Ok!"

@app.route('/<question>')
def questions_answering(question):
    texts = WikiSearch.search(question)
    answers = QAModel.predict(question, texts)
    d = {}
    for i in range(len(answers)):
        d[i] = answers[i]
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0')