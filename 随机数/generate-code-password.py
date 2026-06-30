# 生成随机验证码 随机密码

import random

def generate_code_password(length=6, include_letters=True, include_digits=True, include_symbols=False, case='upper'):

    """
    生成随机验证码/自定义密码

    Args:
        length: 验证码长度 默认为 6
        include_letters: 是否包含字母 默认包含
        include_digits: 是否包含数字 默认包含
        include_symbols: 是否包含特殊符号 默认不包含
        case: 字母大小写模式 默认大写

    Returns:
        
        str: 验证码/密码

    """

    chars = ''     # 初始化空字符串

    if include_digits:
        chars += '0123456789'

    if include_letters:
        if case == 'upper':
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif case == 'lower':
            chars += 'abcdefghijklmnopqrstuvwxyz'
        elif case == 'both':
            chars += 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    
    if include_symbols:
        chars += '!@#$%^&*()_+-=[]{}|;:,.<>?/~'

    if not chars:
        return ''
    
    return ''.join(random.choice(chars) for _ in range(length))


def run_app():

    print("===================== Maxwell 验证码密码生成器 ======================")

    while True:

        print("\n请选择生成类型:")
        print("1. 纯数字 6 位")
        print("2. 纯大写字母 6 位")
        print("3. 纯小写字母 6 位")
        print("4. 数字 + 大写字母 6 位")
        print("5. 数字 + 小写字母 6 位")
        print("6. 自定义长度 数字 + 大小写字母")
        print("7. 自定义密码 数字 + 大小写字母 + 特殊符号")
        print("8. 退出程序")

        choice = input("请输入选项 1 - 8: \n")

        if choice == '1': # 纯数字
            code = generate_code_password(6, include_digits=True, include_letters=False, include_symbols=False)
            print(f"\n验证码: {code}")
            print("-" * 63)


        elif choice == '2': # 纯大写字母
            code = generate_code_password(6, include_digits=False, include_letters=True, include_symbols=False, case='upper')
            print(f"\n验证码: {code}")
            print("-" * 63)


        elif choice == '3': # 纯小写字母
            code = generate_code_password(6, include_digits=False, include_letters=True, include_symbols=False, case='lower')
            print(f"\n验证码: {code}")
            print("-" * 63)


        elif choice == '4': # 数字 + 大写字母
            code = generate_code_password(6, include_digits=True, include_letters=True, include_symbols=False, case='upper')
            print(f"\n验证码: {code} ")
            print("-" * 60)

        
        elif choice == '5': # 数字 + 小写字母
            code = generate_code_password(6, include_digits=True, include_letters=True, include_symbols=False, case='lower')
            print(f"\n验证码: {code}")
            print("-" * 60)


        elif choice == '6': # 自定义长度 数字 + 大小写字母
            try:
                length = int(input("请在此输入验证码的长度: \n"))
                if length <= 0:
                    print("验证码长度必须大于0")
                    continue

                else:
                    code = generate_code_password(length, include_digits=True, include_letters=True, include_symbols=False, case='both')
                    print(f"\n验证码: {code}")
                    print("-" * 60)

            except ValueError:
                print("请输入有效的验证码长度（整数）")

        
        elif choice == '7': # 自定义密码长度 数字 + 大小写字母 + 特殊字符

            try:
                length = int(input("请输入密码的长度: \n"))
                if length <= 0:
                    print("密码长度必须大于0")
                    continue

                else:
                    code = generate_code_password(length, include_digits=True, include_letters=True, include_symbols=True, case='both')
                    print(f"\n密码为: {code}")
                    print("-" * 63)

            except ValueError:
                print("请输入有效的密码长度（整数）")

        elif choice == '8': # 退出程序
            print("感谢使用！再见！")
            break


        else:
            print("无效选项，请选择正确的选项")

run_app()

