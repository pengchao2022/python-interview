# 编写一个猜随机数字的游戏

import random

def guess_number(user_number, computer_number):

    try:
        number = int(user_number)

    except ValueError:
        return "输入有误，请输入有效的数字0-100 或者输入命令退出"
    
    if number > computer_number:
        return "你猜大了，目标数字在 0 - 100 之间"
    
    elif number < computer_number:
        return "你猜小了，目标数字在 0 - 100 之间"
    
    else:
        return "恭喜你！ 答对了！"
    

def run_app():

    print("============== 猜数游戏 ===================")
    print("输入 exit 或者 quit 退出游戏")
    print("====== Designed by Maxwell @2026 =========")

    computer_number = random.randint(1, 100) # 随机取 1 - 100 之间的整数，只生成一次 包含1 和 100
    attempts = 0

    while True:
        user_number = input("请在此输入您的数字0-100 或者输入退出命令退出游戏：\n")

        if user_number.lower() in ['exit', 'quit']:
            print("感谢使用猜数游戏！ 再见！")
            break

        else:
            attempts += 1
            result = guess_number(user_number, computer_number)
            print(result)

        if "恭喜你" in result:
            print(f"您一共尝试了 {attempts} 次")
            break


run_app()

