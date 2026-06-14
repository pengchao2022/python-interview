# filter() 函数用于过滤原色

# even numbers 偶数
# odd numbers

def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 在列表中找出所有 偶数
even_list = list(filter(is_even, numbers))

print(even_list)


# 输出结果为: [2, 4, 6, 8]




