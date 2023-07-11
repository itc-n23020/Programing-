result1 = pow(*divmod(20, 3))
print(result1)

# 複数行だった場合
result = divmod(20, 3)
result2 = pow(result[0], result[1])
print(result2)
