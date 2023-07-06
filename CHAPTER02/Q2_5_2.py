answer = """◯ ● ● ●
● ◯ ● ●
● ● ◯ ●
● ● ● ◯
"""
print(answer)

w = "◯ "
b = "● "
answer1 = ""
for i in range(4):
    for j in range(4):
        if i == j:
            answer1 += w
        else:
            answer1 += b
    answer1 += "\n"
print(answer1)
