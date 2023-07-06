my_list1 = ["I", "have", "an", "apple"]
my_list1[2:4] = ["a", "pineapple"]
print(my_list1)

# 別解１
my_list2 = ["I", "have", "an", "apple"]
my_list2[2:] = ["a", "pineapple"]
print(my_list2)

# 別解２
my_list3 = ["I", "have", "an", "apple"]
my_list3[2] = "a"
my_list3[3] = "pineapple"
print(my_list3)
