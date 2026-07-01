# 编写一个程序，从 1 到 1000 之间（含 1 和 1000）找出所有能被 5 和 7 同时整除的数字，然后随机选择 8 个组成列表并输出。


import random

numbers = [x for x in range(1, 1001) if x % 5 == 0 and x % 7 == 0]


result = random.sample(numbers, 8)

print(result)

