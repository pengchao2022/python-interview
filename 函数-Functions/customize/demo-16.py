# 编写一个程序，接受一个字符串作为输入，如果该字符串是 "yes"、"YES" 或 "Yes"，则打印 "Yes"，否则打印 "No"。

def change_char(input_str):

    if input_str == "yes" or input_str == "YES" or input_str == "Yes":

        return "Yes"
    
    else:

        return "No"
    


def run_app():

    my_str = input("请在此输入您的字符串: ")

    expect_str = change_char(my_str)

    print(expect_str)



run_app()

