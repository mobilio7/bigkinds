from flask import Flask, request, jsonify
from flask.templating import render_template

from sentence_transformers import SentenceTransformer
from transformers import BertTokenizer, BertModel

from predict_module import summarize_test
from baikal_tagger import nlp_tagger
from keyword_module import keyword_ext

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/get_summary", methods=['POST'])
def summary(): # 기사 요약
    test_context = request.form['sentences']
    rtn = summarize_test(test_context)
    response = dict()
    response['result'] = rtn # 결과 문자열

    return jsonify(response), 200

@app.route("/get_tag", methods=['POST'])
def tag(): # 형태소 분석
    test_context = request.form['text']
    res = nlp_tagger(test_context)
    response = dict()
    response['result'] = res # 결과 문자열

    return jsonify(response), 200

@app.route("/get_keyword", methods=['POST'])
def keyword(): # 키워드 추출
    test_context = request.form['text']
    rtn = keyword_ext(test_context)
    response = dict()
    response['result'] = rtn # 결과 문자열

    return jsonify(response), 200

@app.route("/get_sbert", methods=['POST'])
def sbert(): # SBERT model
    rtn = SentenceTransformer('./kpfSBERT') 
    response = dict()
    response['result'] = rtn # SBERT model return

    return jsonify(response), 200

@app.route("/get_bert_tokenizer", methods=['POST'])
def bert_tokenizer(): # BERT tokenizer
    rtn = BertTokenizer.from_pretrained('./kpfbert')
    response = dict()
    response['result'] = rtn # BERT tokenizer return

    return jsonify(response), 200

@app.route("/get_bert", methods=['POST'])
def bert(): # BERT 
    rtn = BertModel.from_pretrained('./kpfbert', add_pooling_layer=False)
    response = dict()
    response['result'] = rtn # BERT model return

    return jsonify(response), 200


@app.route('/temp')
def temp():
    return render_template('input_test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
