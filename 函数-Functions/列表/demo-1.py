# 从控制台输入一连串数字，数字之间以逗号隔开，然后输出一个列表和一个元组

def generate_list_tuple(str1):

    # 首先将字符串转换为列表，以 逗号 分隔
    temp_list = str1.split(',')

    # 去掉列表中字符左右的空格
    new_list = [num.strip() for num in temp_list]

    # 将列表转换成元组
    new_tuple = tuple(new_list)

    return new_list, new_tuple



# 定义个函数运行用户输入
def app_run():
    user_input = input("请在此输入一连串数字，数字之间以逗号分隔:  ")
    # 调用生成函数
    # 设置两个变量用于接收返回值
    my_list, my_tuple = generate_list_tuple(user_input)
    print(my_list)
    print(my_tuple)


# 调用函数
app_run()


