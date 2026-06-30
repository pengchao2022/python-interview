# 编写一个程序，从列表 [5,6,77,45,22,12,24] 中移除所有偶数，然后打印剩下的列表。

def get_odd_list(li):

    odd_list = []

    for i in li:

        if i % 2 != 0:

            odd_list.append(i)

    return odd_list


li = [5,6,77,45,22,12,24] 

print(get_odd_list(li))

