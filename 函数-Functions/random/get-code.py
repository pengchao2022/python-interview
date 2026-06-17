# 获取一个随机的6位数验证码

import random

def generate_code():

    code = "" # 设置一个空字符串接收6位数字

    for x in range(6): # 6 位数验证码
        code += str(random.randint(0, 9))

    return code


def run_app():
    verification_code = generate_code()
    print(verification_code)


run_app()

