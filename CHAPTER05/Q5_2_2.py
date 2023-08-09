# 以下のプログラムを実行した際の出力結果として正しいものは、どれでしょうか？

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
[x if x % 2 == 0 else None for x in list1]

① [4, 6, 8]
② [1, None, 3, None, 5, None, 7, None, 9]
③ [[None, 2, None, 4, None, 6, None, 8, None]]
④ [None, 2, None, 4, None, 6, None, 8, None]

# 正解:④
