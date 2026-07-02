# 在指文章中全局查找 指定的 字符或者字符串

def find_and_count(text, substring):

    index_list = []
    start = 0

    while True:

        index = text.find(substring, start)

        if index == -1:

            break

        else:

            index_list.append(index)

            start = index + 1

    count = len(index_list)

    return count, index_list


def run_app():

    text = input("请在此输入您的文章或者语句:").strip()

    substring = input("请在此输入您要查找的字符或者字符串:")

    count, index_list = find_and_count(text, substring)

    if count == 0:

        print("抱歉！ 没有找到改字符或者字符串")

    else:

        print(f"{substring} 共出现了 {count} 次")

        print(f"索引列表为: {index_list}")

    return None

run_app()

