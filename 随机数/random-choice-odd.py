# 编写一个程序，使用 random 模块和列表推导式，生成并输出一个 0 到 10 之间的随机偶数（包含 0 和 10）。

import random


expect_num = random.choice([x for x in range(11) if x % 2 != 0])

print(expect_num)

