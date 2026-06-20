# 题目： 一个网站要求用户输入用户名和密码进行注册。编写一个程序来检查用户输入的密码的有效性。密码检查标准如下：

# 至少包含 1 个小写字母 [a-z]

# 至少包含 1 个数字 [0-9]

# 至少包含 1 个大写字母 [A-Z]

# 至少包含 1 个来自 [$#@] 的特殊字符

# 密码最小长度：6

# 密码最大长度：12

# 您的程序应接受一串以逗号分隔的密码序列，并根据上述标准进行验证。符合标准的密码需要打印出来，每个密码用逗号分隔。

import re

def check_passwrod_validation(password):

    # 检查密码的有效性 需要符合上面的条件

    # 检查密码长度
    if not (6 <=len(password) <= 12):
        return False
    
    # 检查是否有数字
    if not re.search(r'[0-9]', password):
        return False
    
    # 检查是否有小写字母
    if not re.search(r'[a-z]', password):
        return False
    
    # 检查是否有大写字母
    if not re.search(r'[A-Z]', password):
        return False
    
    # 检查是否包含上述特殊字符
    if not re.search(r'[$#@]', password):
        return False
    
    else:
        return True
    

def validate_passwords(input_str):

    # 将用户输入的字符串转换为列表
    passwords = [p.strip() for p in input_str.split(',')]

    # 筛选出所有有效的密码
    valid_passwords = [p for p in passwords if check_passwrod_validation(p)]

    # 以逗号隔开输出到一行字符串
    return ','.join(valid_passwords)

def run_app():

    user_input = input("请在此输入连续的密码并以逗号隔开: ")

    expect_password = validate_passwords(user_input)

    print(expect_password)


run_app()



