# 定义一个列表，打印出列表中的所有的偶数并以列表形式输出

demo_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


odd_list = list(filter(lambda x: x % 2 != 0, demo_list))

print(odd_list)


even_list = list(filter(lambda x: x % 2 == 0, demo_list))

print(even_list)

