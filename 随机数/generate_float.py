# 生成指定个数的浮点数生成器

import random

def generate_random_float(min, max):
    """生成指定范围的随机浮点数"""

    return random.uniform(min, max)


def run_app():

    print("===================== Maxwell 浮点数生成器 ========================")

    print("输入 exit 或者 quit 退出程序")

    print("==================================================================")

    while True:

        # 用户输入最小值
        min_input = input("请在此输入最小值 或者输入 exit/quit 退出程序:\n")

        if min_input.lower() in ['exit', 'quit']:
            print("感谢使用，再见！")
            break

        # 处理用户输入
        try:
            min = float(min_input)

        except ValueError:
            print("请输入有效的数字")


        # 用户输入最大值
        max_input = input("请在此输入最大值 或者输入 exit/quit 退出程序:\n")

        if max_input.lower() in ['exit', 'quit']:
            print("感谢使用，再见！")
            break

        # 处理用户输入
        try:
            max = float(max_input)

        except ValueError:
            print("请输入有效的数字")

        # 用户输入生成浮点数的个数
        count_input = input("请在此输入要生成的浮点数的个数 或者输入 exit/quit 退出程序:\n")

        if count_input.lower() in ['exit', 'quit']:
            print("感谢使用！再见！")
            break

        if min >= max:
            print("最大值必须大于最小值")


        # 处理个数
        try:
            count = int(count_input)

        except ValueError:
            print("请输入有效的整数")

        
        if count == 0:
            print("生成浮点数的个数必须大于 0 ")

        
        # 生成指定个数的随机浮点数
        print(f"生成{count}个随机浮点数")
        for i in range(count):
            num = generate_random_float(min, max)
            print(f"随机数{i + 1:2d}: {num:.2f} ") # 小数点后保留两位小数

        print("-" * 60)

        again = input("\n是否继续生成 y/n:").lower()

        if again not in ['y', 'yes']:
            print("感谢使用！ 再见！")
            break


run_app()



