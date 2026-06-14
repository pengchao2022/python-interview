# all() 判断列表元素为true or false

def check_list(numbers):
    return all(x > 0 for x in numbers) # 判断列表里面的元素是否是正数

list1 = [98, 76, 4, 2, 34]

list2 = [-9, 0, 78, -200]

print(check_list(list1))
print(check_list(list2))


# 输出结果为：
# True
# False
