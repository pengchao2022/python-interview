# 给定两个列表 [1,3,6,78,35,55] 和 [12,24,35,24,88,120,155]，编写一个程序，找出两个列表中都存在的元素，生成一个新列表并打印。

given_list_1 = [1,3,6,78,35,55]

given_list_2 = [12,24,35,24,88,120,155]

set_1 = set(given_list_1)

set_2 = set(given_list_2)

# 求交集
both_value_list = list(set_1 & set_2)

# 求并集
union_list = list(set_1 | set_2)


print(f"交集为: {both_value_list}")

print(f"并集为: {union_list}")


