# 请使用 Python 的 random 模块生成一个 5 到 95 之间的随机浮点数。

# 提示：使用 random.random() 可以生成一个 0 到 1 之间的随机浮点数（包含 0，不包含 1）。


import random

expect_float1 = random.uniform(5, 95)

expect_float2 = round(expect_float1, 2) # round 函数 保留两位小数

print(expect_float1)

print(expect_float2)

