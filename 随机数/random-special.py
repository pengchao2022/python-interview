# 编写一个程序，使用 random 模块和列表推导式，从 0 到 10 之间（包含 0 和 10）的整数中，随机输出一个既能被 5 整除又能被 7 整除的数

import random

expect_num = random.choice([x for x in range(11) if x % 5 == 0 and x % 7 ==0])


print(expect_num)


