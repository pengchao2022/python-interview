# 写一个倒计时函数

# 从指定数字开始倒计时

# 输出在一行

# 输出最后加上 blast off!

def countdown(start_num):

    while start_num > 0:

        print(start_num, end=' ')

        start_num -= 1

    print('Blast Off!')


def run_app():

    start_num = int(input("请在此输入您的开始数字: \n"))

    countdown(start_num)


if __name__ == "__main__":

    run_app()

    