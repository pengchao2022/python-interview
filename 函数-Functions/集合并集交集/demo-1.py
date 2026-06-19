# 定义两个列表，求 交集，并集，差集

list_a = [89, 45, 35, 2, 6, 90, 35]

list_b = [1, 2, 3, 4, 5, 6, 2]



# 注意 列表本身是没有交集等操作的， 要先转换为集合，再进行集合拥有的操作

# 转换为集合

set_a = set(list_a)

set_b = set(list_b)

# 两个集合的交集

intersection = set_a & set_b

print(f"交集为: {intersection}")

# 两个集合的差集

difference = set_a - set_b

print(f"差集为: {difference}")

# 两个集合的并集
union = set_a | set_b     # 并集是唯一的， 在集合里面元素不允许重复

print(f"并集为: {union}")
