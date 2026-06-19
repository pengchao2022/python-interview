# 定义一个整数列表，使用列表推导式 打印出所有奇数，并以列表显示

demo_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

odd_list = [x for x in demo_list if x % 2 != 0]


print(f"奇数列表为: {odd_list}")

# 所有的偶数
even_list = [x for x in demo_list if x % 2 == 0]

print(f"偶数列表为: {even_list}")





