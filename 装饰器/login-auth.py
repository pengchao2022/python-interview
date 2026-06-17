# 写一个登录的装饰器
def auth(func):
    def inner(*args, **kwargs): # 接收所有位置参数，和关键字参数

        # 情况1 位置参数
        if len(args) >= 2:
            username = args[0]
            password = args[1]

        # 情况2 关键字参数
        else:
            username = kwargs.get('username')
            password = kwargs.get('password')

        # 验证逻辑判断
        if username == 'admin' and password =='123':
            print("登录成功")
            return func(*args, *kwargs)
        
        else:
            print("登录失败")
            return None
        
    # 内部函数暴露给外部使用
    return inner


# 定义主函数并调用装饰器
@auth
def my_app(username, password):
    return f"欢迎！{username}, 您的密码是: {password}"



# 定义运行函数
def run_app():
    username = input("Please enter your username here:")
    password = input("Please enter your password here:")
    result = my_app(username, password) # 把 接收到的数据传递给主函数
    if result:  # 如果 result不是None 或空字符串就会执行打印
        print(result)



# 调用运行函数
run_app()


