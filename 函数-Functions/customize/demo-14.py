# 定义一个函数，该函数能够生成一个列表，其中列表的值是1到20之间（包含两端）数字的平方。然后该函数需要打印列表中除了前5个元素之外的所有值。

def num_square_list():

    square_list = [i ** 2 for i in range(1, 21)]

    expect_list = square_list[5::]

    return expect_list



print(num_square_list())

