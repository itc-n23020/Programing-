import string
from random import randint

result = [chr(ord("A") + i) for i in range(26)]
print(randint(result))
