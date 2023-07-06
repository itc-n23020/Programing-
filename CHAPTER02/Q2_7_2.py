# 昇順
my_list1 = ["orange", "apple", "grape", "banana"]
my_list1.sort()
print(my_list1)

# 昇順(別解)
my_list3 = ["orange", "apple", "grape", "banana"]
my_list3 = sorted(my_list3)
print(my_list3)

# 降順
my_list2 = ["orange", "apple", "grape", "banana"]
my_list2.sort(reverse=True)
print(my_list2)

# 降順(別解)
my_list4 = ["orange", "apple", "grape", "banana"]
sorted_list = sorted(my_list4, reverse=True)
print(sorted_list)
