my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = my_list[::-2]
print(result)

# 別解１
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
reverse_even = my_list1[-2::-2]
print(reverse_even)

# 別解２
numbers = list(range(1, 11))

even_numbers = [num for num in numbers if num % 2 == 0]
reversed_numbers = even_numbers[::-1]

print(reversed_numbers)
