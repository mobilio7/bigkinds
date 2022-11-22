from flask import Flask, request, jsonify
from flask.templating import render_template

from predict_module import summarize_test
from baikal_tagger import nlp_tagger

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

@app.route('/temp')
def temp():
    return render_template('input_test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
