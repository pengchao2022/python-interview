# 写一个程序 生成一个包含5 个随机整数的列表，这些整数来自 100 - 200

# 使用列表推导式

import random

expect_list = [random.randint(100, 200) for _ in range(5)]

print(expect_list)

