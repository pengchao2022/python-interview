# 编写一个程序，随机生成一个包含 5 个偶数的列表，这些偶数的范围在 100 到 200 之间（含 100 和 200）。

# 使用列表推导式

import random

expect_list = [random.randrange(100, 201, 2) for _ in range(5)]

print(expect_list)


