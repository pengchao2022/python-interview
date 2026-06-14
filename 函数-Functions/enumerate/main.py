# enumerate() 列出列表里的索引和元素

my_list = [90, 45, 78, 3, 120, 119, 200]

for index, element in enumerate(my_list):
    print(index, element)


# 输出结果为
# 0 90
# 1 45
# 2 78
# 3 3
# 4 120
# 5 119
# 6 200

names = ['kate', 'lily', 'sophia', 'carol']

ages = [27, 46, 24, 50]

for number, name in enumerate(names, start=1):
    print(number, name)

# 1 kate
# 2 lily
# 3 sophia
# 4 carol