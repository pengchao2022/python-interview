# 编写一个程序，接收一串以逗号分隔的4位二进制数作为输入，然后检查它们是否能被 5 整除。所有能被 5 整除的数字，要以逗号分隔的序列形式输出。

# 示例：
# 输入：

# text
# 0100,0011,1010,1001
# 输出应该是：

# text
# 1010

def check_binary_number(input_str):

    # 将用户的输入字符串以空格分割
    binary_list = input_str.split(',')

    # 定义一个空列表来存储符合条件的binary 
    result = []

    for binary in binary_list:
        
        # 将二进制转换为 十进制
        decimal = int(binary, 2)

        # 判断是否能被5整除
        if decimal % 5 == 0:
            result.append(binary)

    return ','.join(result)


def run_app():
    user_input = input("请在此输入连续的二进制数并以逗号分隔: ")
    expect_binary = check_binary_number(user_input)

    print(expect_binary)


run_app()



