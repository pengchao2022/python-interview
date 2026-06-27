# 定义一个函数，该函数能够生成并打印一个元组，其中元组的值是1到20之间（包含两端）数字的平方。

def num_square_list():

    square_list = [i ** 2 for i in range(1, 21)]

    expect_tuple = tuple(square_list)

    return expect_tuple



print(num_square_list())

