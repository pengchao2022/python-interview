# 定义一个函数，该函数能够生成并打印一个列表，其中列表的值是1到20之间（包含两端）数字的平方。

# 使用列表推导式

def num_square_list():

    square_list = [i ** 2 for i in range(1, 21)]

    return square_list



print(num_square_list())


