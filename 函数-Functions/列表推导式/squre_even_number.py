# 题目： 使用列表推导式对列表中的每个奇数求平方。该列表通过逗号分隔的数字序列输入。

# 假设程序接收以下输入：

# text
# 1,2,3,4,5,6,7,8,9
# 那么输出应为：

# text
# 4,16,36,64

def squre_even_number(input_str):

    # 将输入的字符串编程整数列表，并去掉字符前后的空格

    numbers = [int(x.strip()) for x in input_str.split(',')]

    # 推导式求偶数的平方

    result = [str(x**2) for x in numbers if x % 2 == 0]

    return ','.join(result)


def run_app():
    
    user_input = input("请在此输入一连串数字并以逗号分隔: ")

    expect_result = squre_even_number(user_input)

    print(expect_result)


run_app()

