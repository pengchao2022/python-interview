# 请编写一个程序，打印出 [1, 2, 3] 的所有排列组合。

import itertools

my_list = [1, 2, 3]

for p in itertools.permutations(my_list):

    print(list(p))

    

