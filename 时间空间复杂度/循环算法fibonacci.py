# 斐波那契数列按以下公式计算：
# 当 n = 0 时，f(0) = 0
# 当 n = 1 时，f(1) = 1
# 当 n > 1 时，f(n) = f(n-1) + f(n-2)
# 请编写一个程序，使用列表推导式生成斐波那契数列，并以逗号分隔的格式输出，n 由用户在控制台输入。
# 示例：如果输入 n = 7，程序应输出 0,1,1,2,3,5,8,13（共 n+1 项，从 0 到 7）。


def fibonacci(n):
    """使用循环计算第 n 个斐波那契数（高效版本）"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1  # f(0)=0, f(1)=1
    for _ in range(2, n + 1):
        a, b = b, a + b  # 更新：f(i) = f(i-1) + f(i-2)
    return b


def get_list(n):
    """生成斐波那契数列并返回逗号分隔的字符串"""
    new_list = [str(fibonacci(i)) for i in range(0, n + 1)]
    return ','.join(new_list)


def run_app():
    num = int(input("请在此输入一个数字: "))
    result = get_list(num)
    print(result)


run_app()