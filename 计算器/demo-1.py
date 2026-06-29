# 编写一个程序，接收用户在控制台输入的基本数学表达式（如加减乘除），然后计算并输出结果, 需要循环并可以退出程序。

# 示例：如果输入 35+3，程序应输出 38。

def calculator(expression):

    if '+' in expression:

        parts = expression.strip().split('+')

        return float(parts[0]) + float(parts[1])
    
    elif '-' in expression:

        parts = expression.strip().split('-')

        return float(parts[0]) - float(parts[1])
    
    elif '*' in expression:

        parts = expression.strip().split('*')

        return float(parts[0]) * float(parts[1])
    

    elif '/' in expression:

        parts = expression.strip().split('/')

        if float(parts[1]) == 0:

            return "Error: 除数不能为零！"
        
        else:

            return float(parts[0]) / float(parts[1])
        

    else:

        return "Error: 输入错误! 请按照这样的表达式 如: 1 + 2"


def run_app():

    print("================ Maxwell Calculator =====================")
    print("输入 exit 或者 quit 退出程序")
    print("=========================================================")

    while True:

        expression = input("请在此输入您的表达式 如：1 + 2 \n")

        if expression.lower() in ['exit', 'quit']:
            print("欢迎再次使用，再见！")
            break

        else:
            result = calculator(expression)
            print(result)


run_app()


