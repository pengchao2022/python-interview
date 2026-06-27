# 编写一个程序，使用 map() 函数生成一个列表，该列表的元素是 [1,2,3,4,5,6,7,8,9,10] 中每个元素的平方。

def square(num):

    return num ** 2


my_list = [1,2,3,4,5,6,7,8,9,10]

result = map(square, my_list)

expect_list = list(result)

print(expect_list)

