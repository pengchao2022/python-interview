# 定义一个函数，生成一个字典，字典的键是1到20之间的数字（含1和20），对应的值是键的平方。这个函数只需打印出字典中的所有键（不打印值）。

def num_square_dict():

    square_dict = {}

    for i in range(1, 21):

        square_dict[i] = i ** 2

    key_list = []

    for key in square_dict:
        key_list.append(str(key))

    return ','.join(key_list)


print(num_square_dict())

