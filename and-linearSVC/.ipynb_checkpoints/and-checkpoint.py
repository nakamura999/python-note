{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## AND演算を機械学習するプログラム"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0], [1, 0], [0, 1], [1, 1]] ー予測の結果 [0 0 0 1]\n",
      "正解率 = 1.0\n"
     ]
    }
   ],
   "source": [
    "# ライブラリのインポート\n",
    "from sklearn.svm import LinearSVC\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# 学習用のデータと結果\n",
    "# X,Y\n",
    "learn_data = [[0,0], [1,0], [0,1], [1,1]]\n",
    "# X and Y\n",
    "learn_label = [0, 0, 0, 1]\n",
    "\n",
    "# アルゴリズムの指定(LinearSVC)\n",
    "clf = LinearSVC()\n",
    "\n",
    "# 学習用データと結果の学習\n",
    "clf.fit(learn_data, learn_label)\n",
    "\n",
    "# テストデータによる予測\n",
    "test_data = [[0,0], [1,0], [0,1], [1,1]]\n",
    "test_label = clf.predict(test_data)\n",
    "\n",
    "# 予測結果の評価\n",
    "print(test_data, 'ー予測の結果', test_label)\n",
    "print('正解率 =', accuracy_score([0, 0, 0, 1], test_label))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
