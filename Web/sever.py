import json
import flask
from flask import request
import my_text

# ポート番号
TM_PORT_NO = 8085
# HTTPサーバーを起動
app = flask.Flask(__name__)
print("http://localhost:" + str(TM_PORT_NO))

# ルートへアクセスした場合
@app.route('/', methods=['GET'])
def index():
	with open('index.html', 'rb') as f:
		return f.read()

# /api へアクセスした場合
@app.route('/api', methods=['GET'])
def api():
	# URLパラメータを取得
	q = request.args.get('q', '')
	if q == '':
		return '{"label": "空です", "per": 0}'
	print('q=', q)
	# テキストのジャンル判定を行う
	label, per, no = my_text.cheak_genre(q)
	# 結果をjsonで出力
	return json.dumps({})
