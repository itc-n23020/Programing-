# 以下のプログラムを実行した際の出力結果として正しいものは、どれでしょうか？
 def test_function():
     try:
         print('try')
         return
     except:
         print('except')
    else:
        print('else')
    finally:
        print('finally')

test_function()

① try
  finally

② try
  except
  else
  finally

③ try
  else
  finally

④ finally

# 解答 ①
