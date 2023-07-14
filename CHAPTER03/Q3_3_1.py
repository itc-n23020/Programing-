my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
print(my_list_6)

# 別解
my_list = ["tokyo", "osaka", "fukuoka", "aichi", "kyoto", "chiba", "saitama", "gunma"]
filtered_list = [word for word in my_list if len(word) >= 6]
print(filtered_list)
