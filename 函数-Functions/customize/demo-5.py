# 定义一个函数，该函数能够接受两个字符串作为输入，并在控制台中打印出长度最长的那个字符串。如果两个字符串长度相同，则该函数应逐行打印所有字符串

def compare_two_strings(str1, str2):

    if len(str1) > len(str2):
        return str1
    
    elif len(str1) < len(str2):
        return str2
    
    else:
        return str1, str2        # python3 中有多个返回值时，会以元组的类型返回
    

def run_app():

    str1 = input("请在此输入第一个字符串: ")
    str2 = input("请在此输入第二个字符串: ")

    result = compare_two_strings(str1, str2)

    if isinstance(result, tuple):
        for s in result:
            print(s)


    else:
        print(result)


# 调用函数

run_app()


    
