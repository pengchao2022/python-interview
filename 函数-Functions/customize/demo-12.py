# 定义一个函数，该函数能够生成一个列表，其中列表的值是1到20之间（包含两端）数字的平方。然后该函数需要打印列表中的最后5个元素。


def num_square_list():

    # 使用列表推导式
    square_list = [i ** 2 for i in range(1, 21)]

    # 定义一个空列表
    back_five = []

    for j in range(len(square_list)):

        if j >= 15 and j <= 20:

            back_five.append(square_list[j])

    return back_five


print(num_square_list())

