# 编写一个程序，生成并打印另一个元组，该元组的值是给定元组 (1,2,3,4,5,6,7,8,9,10) 中的奇数。

def odd_tuple(my_tuple):

    new_list = []

    for i in my_tuple:

        if i % 2 != 0:

            new_list.append(str(i))

    expect_tuple = tuple(new_list)

    return expect_tuple


my_tuple = (1,2,3,4,5,6,7,8,9,10)

print(odd_tuple(my_tuple))

