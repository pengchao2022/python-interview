# 定义一个函数，该函数能够生成一个列表，其中列表的值是1到20之间（包含两端）数字的平方。然后该函数需要打印列表中的前5个元素。

def num_square_list():

    square_list = [i ** 2 for i in range(1, 21)]

    first_five = []

    for j in range(len(square_list)):

        if j <= 4:

            first_five.append(square_list[j])

    return first_five


print(num_square_list())


