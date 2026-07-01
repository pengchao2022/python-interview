# 请使用列表推导式，编写一个程序，从列表 [12,24,35,70,88,120,155] 中移除索引为 0、4、5 的元素（即第 1、5、6 个元素），然后打印剩下的列表。


user_list = [12,24,35,70,88,120,155]

removed_index = [0, 4, 5]


expect_list = [x for i, x in enumerate(user_list) if i not in removed_index]


print(expect_list)

