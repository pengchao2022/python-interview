# 编写一个程序，接收用户在控制台输入的字符串，然后提取并打印所有索引为偶数（0, 2, 4, 6, ...）的字符。

# 示例：如果输入 H1e2l3l4o5w6o7r8l9d，程序应输出 Helloworld。

def get_even_elem(user_list):

    expect_list = [x for i, x in enumerate(user_list) if i % 2 == 0]

    return ''.join(expect_list)



def run_app():

    user_input = input("请在此输入一个连续的字符串: \n")

    user_list = list(user_input.strip())

    result = get_even_elem(user_list)

    print(result)


run_app()

