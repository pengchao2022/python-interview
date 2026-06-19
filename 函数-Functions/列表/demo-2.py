# 题目要求，输入一连串单词，中间以逗号隔开
# 按照单词首字母排序，并输出一个字符串，以逗号隔开

def change_order(str1):

    # 去掉用户输入的字符串前后的空格
    clean_str = str1.strip()

    # 将字符串以逗号分隔成列表
    temp_list = clean_str.split(',')

    # 将列表各个字符左右的空格去掉
    clean_list = []
    for word in temp_list:
        clean_list.append(word.strip())

    # 将列表里面的字符以首字母排序
    sorted_lsit = sorted(clean_list)

    return sorted_lsit


# 定义一个函数接收并打印用户输入
def run_app():
    user_input = input("Please enter several words here seprated with ',': ")
    order_list = change_order(user_input)
    except_str = ','.join(order_list)

    print(except_str)


run_app()

