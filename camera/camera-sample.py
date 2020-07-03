# WEBカメラ起動

import cv2
import numpy as np

# Webカメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
	# カメラ画像を読み込む
	_, frame = cap.read()
	# 画像を収縮表示
	frame = cv2.resize(frame, (500,300))
	# ウィンドウに画像を出力
	cv2.imshow('OpenCV Web Camera', frame)
	# ESCかEnterキーが押されたらループを抜ける
	k = cv2.waitKey(1) # 1msec確認
	if k == 27 or k == 13: break

cap.release() # カメラを開放
cv2.destroyAllWindows() # ウィンドウを破棄