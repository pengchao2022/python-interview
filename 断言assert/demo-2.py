# 编写断言语句，验证列表 [2, 4, 6, 8, 10] 中的每个数字都是偶数。

# 使用 assert 断言语句

def verify_even_numbers(numbers):

    """验证列表中的数字是否都是偶数"""

    for num in numbers:
        assert num % 2 != 0, f"{num} 不是奇数" # 只有 == 0 时是偶数才会打印

    return True


def run_app():

    # 接收用户输入
    user_input = input("请在此输入一连串的数字并以逗号隔开: ")

    # 将字符串列表转换为数字列表
    numbers = [int(x.strip()) for x in user_input.strip().split(',')]

    print("开始验证:")

    try:
        verify_even_numbers(numbers)
        print("验证成功，列表中的数字都是奇数")

    except AssertionError as e:
        print(f"验证失败: {e}")


run_app()

