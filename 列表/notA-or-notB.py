# 请使用列表推导式，编写一个程序，从列表 [12,24,35,70,88,120,155] 中移除所有能被 5 和 7 同时整除的数，然后打印剩下的列表。

user_list = [12,24,35,70,88,120,155]

expect_list = [x for x in user_list if x % 5 != 0 or x % 7 != 0] 


print(expect_list)

