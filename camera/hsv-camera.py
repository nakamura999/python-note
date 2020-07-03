import cv2
import numpy as np

# webカメラから入力を開始
cap = cv2.VideoCapture(0)
while True:
	# 画像を取得して縮小
	_, frame = cap.read()
	frame = cv2.resize(frame, (500,300))
	# 色空間をHSVに変換
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
	# HSVを分割
	h = hsv[:, :, 0]
	s = hsv[:, :, 1]
	v = hsv[:, :, 2]
	# 赤色っぽい色を持つ色素だけを抽出
	img = np.zeros(h.shape, dtype=np.uint8)
	img[((h < 50) | (h > 200)) & (s > 100)] = 255
	# ウィンドウに画像を出力
	cv2.imshow('RED Camere', img)
	if cv2.waitKey(1) == 13: break

cap.release()
cv2.destroyAllWindows()


# Hue(色相)で赤と言えば、紫っぽい範囲まで含めれば 280〜28°くらい。これを256段階に計算し直すと、200〜50くらいになる。なので、Hの値が (H < 20 | H > 200) の範囲が赤色
# S(彩度)も同時に判定する必要がある。0〜255の範囲で、数値が大きくなればなるほど「鮮やか」という事。ここでは、赤色の判定なので、Sの値が (S > 100) である事を条件としている