# 编写一个程序，使用生成器生成 0 到 n 之间所有能被 5 和 7 同时整除（即能被 35 整除）的数字，并以逗号分隔的格式输出，n 由用户在控制台输入。

# 示例：如果输入 n = 100，程序应输出 0,35,70。


def generate_expect_numbers(n):

    """使用生成器 筛选符合条件的数字"""

    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i       # yield 暂停函数，返回一个值


def get_expect_string(n):

    return ','.join([str(i) for i in generate_expect_numbers(n)]) # 列表推导式 return 结束函数 返回一个值


def run_app():

    num = int(input("请在此输入一个数字: "))
    result = get_expect_string(num)
    print(result)

run_app()

