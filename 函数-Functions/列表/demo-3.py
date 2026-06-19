# 属于几行英文语句
# 将英文语句转换为大写后输出

def multi_line_in_out():

    print("请在此输入英文语句并以空行结束: ")

    lines = [] # 定义一个空列表用来存储输入

    while True:

        line = input()

        if line == "": # 空行结束
            break

        lines.append(line)


    # 将句子都转换为大写
    for line in lines:
        print(line.upper())


multi_line_in_out()

