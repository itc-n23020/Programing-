import pickle

Q3_8_1.pyで作成したファイルから数値を読み込んで、リストに格納するプログラミングを作成してください。

# 解答
with open('test1.pkl', 'rb') as f:
    result = pickle.load(f)
    print = (result)
