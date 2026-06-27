# 定义一个函数，生成一个列表，列表中的元素是1到20之间（含1和20）所有数字的平方。然后该函数需要打印出列表中最后7个元素。


def num_square_list():

    # 使用列表推导式

    square_list = [i ** 2 for i in range(1, 21)]

    back_seven = square_list[-7::]

    return back_seven



print(num_square_list())

