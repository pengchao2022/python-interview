# 编写一个程序，计算 a + aa + aaa + aaaa 的值，其中 a 是一个给定的数字。

# 假设程序接收的输入为：9
# 则输出应为：11106

def same_num_multi_add(num_str):

    num1 = int(num_str*1)

    num2 = int(num_str*2)

    num3 = int(num_str*3)

    num4 = int(num_str*4)

    result = num1 + num2 + num3 + num4

    return result

def run_app():

    num_str = input("请在此输入一个数字0-9: ")

    expected_result = same_num_multi_add(num_str)

    print(expected_result)


run_app()

