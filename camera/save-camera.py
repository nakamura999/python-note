# 動画ファイルの保存

import cv2
import numpy as np

# カメラからの入力を開始
cap = cv2.VideoCapture(0)
# 動画書き出し用のオブジェクトを生成
fmt = cv2.VideoWriter_fourcc('m','p','4','v')
fps = 20.0
size = (640, 360)
writer = cv2.VideoWriter('test.m4v', fmt, fps, size)

while True:
	_, frame = cap.read()
	frame = resize(frame, size)
	# 画面を出力
	writer.write(frame)
	# ウィンドウ上にも表示
	cv.imshow('frame', frame)
	if cv2.waitKey(1) == 13: break

writer.release()
cap.release()
cv2.destroyAllWindows()