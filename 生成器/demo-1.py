# 编写一个程序，使用生成器生成 0 到 n 之间的所有偶数，并以逗号分隔的格式输出，n 由用户在控制台输入。

# 示例：如果输入 n = 10，程序应输出 0,2,4,6,8,10。


def generate_even_numbers(n):

    """使用生成器，生成 0 到 n 之间的所有偶数"""

    for i in range(n + 1):

        if i % 2 == 0:
            yield i         # yield 是返回一个值，暂停函数


def get_even_string(n):

    return ','.join([str(i) for i in generate_even_numbers(n)])


def run_app():

    num = int(input("请在此输入一个数字: "))
    result = get_even_string(num)
    print(result)


run_app()

