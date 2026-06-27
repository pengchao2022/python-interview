# 定义一个函数，该函数能够打印一个字典，其中键是介于1和20之间（包含两端）的数字，值是键的平方


def num_square_dict():

    square_dict = {}

    for i in range(1, 21):

        square_dict[i] = i ** 2


    return square_dict


print(num_square_dict())



