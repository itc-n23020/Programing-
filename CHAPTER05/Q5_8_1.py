# 次のプログラミングを実行したときの出力結果として、正しいものはどれでしょうか？

country_code = {
    'Iceland': {'code': '354', 'capital': 'Reykjavik'},
    'Ireland': {'code': '353', 'capital': 'Dublin'},
    'Azerbaijan': {'code': '994', 'capital': 'Baku'}
}


def getstr_keyval(x):
    if not isinstance(x, dict):
        return x

    my_str = ''
    for key, val in x.item():
        my_str += (' '+str(key)+' '+getstr_keyval(val))
    return my_str


for key1, val1 in country_code.items():
    print(key1, getstr_keyval(val1))


① 順不同
Iceland code, 354 capital Reykjavik Ireland code 353 capital Dublin Azerbaijan code 994 capital, Baku
② 行順不同
Iceland(code 354)(capital Reykjavik)
Ireland(code 353)(capital Dublin)
Azerbaijan(code 994)(capital Baku)
③
Iceland code 354 capital Reyjavik
Ireland code 353 capital Dublin
Azerbaijan code 994 capital Baku
④ 順不同、行順不同
Iceland code 354 capital Reyjavik
Ireland code 353 capital Dublin
Azerbaijan code 994 capital Baku

# 正解:④
