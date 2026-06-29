# 编写一个程序，读取一个 ASCII 字符串，然后将其转换为使用 UTF-8 编码的 Unicode 字符串

def change_to_utf8(text):

    return text.encode('utf-8')


def run_app():
    
    text = input("请在此输入一个字符串: ")

    result = change_to_utf8(text)

    print(result)
    print(type(result))



run_app()
