# 编写一个程序，使用 filter 函数过滤列表中的偶数。列表为：[1,2,3,4,5,6,7,8,9,10]

def is_even(num):

    return num % 2 == 0


my_list = [1,2,3,4,5,6,7,8,9,10]

result = filter(is_even, my_list)

expect_list = list(result)

print(expect_list)

