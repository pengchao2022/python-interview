# 编写一个程序，将列表 [3,6,7,8] 中的元素随机打乱，然后打印打乱后的列表。


import random

my_list = [3, 6, 7, 8]

random.shuffle(my_list) # random shuffle 直接打乱原来列表里面元素的顺序， 没有返回值

print(my_list)