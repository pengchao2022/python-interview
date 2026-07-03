# 输入一个段落 判断里面是否包含数字

def contains_digit(text):

    """
    判断是否包含数字
    """

    for char in text:

        if char.isdigit():

            return True
        
    return False

def run_app():

    text = input("请在此输入您的语句或段落:\n")

    result = contains_digit(text)

    if result:

        print("包含数字")

    else:

        print("不包含数字")


if __name__ == "__main__":

    run_app()

    