# 编写断言语句，验证列表 [1, 3, 5, 7] 中的每个数字都是奇数。

# 使用 assert 断言语句

def verify_odd_numbers(numbers):

    """验证列表里的数字是否为奇数"""

    for num in numbers:
        assert num % 2 != 0, f"{num} 不是奇数"

    return True


def run_app():

    # 接收用户的输入
    user_input = input("请在此输入一连串的数字并以逗号隔开: ")

    # 将字符串输入转换为数字列表        
    numbers = [int(x.strip()) for x in user_input.strip().split(',')]

    print("开始验证:")

    try:
        verify_odd_numbers(numbers)
        print("验证成功！ 所有数字都是奇数")

    except AssertionError as e:
        print(f"验证失败！{e}")

run_app()

