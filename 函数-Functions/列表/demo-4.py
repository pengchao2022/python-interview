# 编写一个程序，接收一串以空格分隔的单词作为输入，然后去除所有重复的单词，并按照字母数字顺序（字母顺序）排序后输出这些单词。

# 假设程序接收到的输入是：

# text
# hello world and practice makes perfect and hello world again
# 那么输出应该是：

# text
# again and hello makes perfect practice world

def change_word_order(str1):

    # 去掉用户输入的多个单词字符串前后空格
    clean_str = str1.strip()

    # 将字符串转换为列表 以空格分隔
    temp_list = clean_str.split()

    # 去掉列表里面单词前后的空格
    clean_list = []
    for word in temp_list:
        clean_list.append(word.strip())

    # 去除重复需要将列表转换为集合
    set_list = set(clean_list)

    # 将集合转换回列表
    new_list = set(set_list)

    # 将列表里面的元素排序
    final_list = sorted(new_list)

    return final_list


def run_app():
    user_input = input("请在此输入多个英文单词中间以空格隔开: ")
    expect_list = change_word_order(user_input)
    expect_str = ' '.join(expect_list)

    print(expect_str)


run_app()
