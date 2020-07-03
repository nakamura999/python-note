# カメラ画像から赤色成分だけを表示
import cv2
import numpy as np

# Webカメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
	# 画像を取得
	_, frame = cap.read()
	# 画像を縮小
	frame = cv2.resize(frame, (500,300))
	# 青と緑の成分を０に、(Numpyのインデックスを利用)
	frame[:, :, 0] = 0 # 青要素を0
	frame[:, :, 1] = 0 # 赤要素を0
	# ウィンドウに画像を出力
	cv2.imshow('RED Camera', frame)
	# Enterキーが押されたらループを抜ける
	if cv2.waitKey(1) == 13: break

cap.release() # カメラを開放
cv2.destroyAllWindows() # ウィンドウを破棄