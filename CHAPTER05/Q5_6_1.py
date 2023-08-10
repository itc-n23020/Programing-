# 以下のプログラムを実行した際の出力結果として正しいものは、どれでしょうか？

a = {x for x in 'abcabcabc' if x not in 'ab'}
b = {y for y in 'abcabcabc' if y not in 'bc'}
print(a | b)

① {'a', 'c'}
② {'b', 'c'}
③ {'a', 'b'}
④ {'c'}

# 正解:①
