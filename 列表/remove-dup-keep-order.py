# 列表去除重复元素，并保持顺序

def remove_dup_keep_order(user_list):


    expect_list = []

    for x in user_list:

        if x not in expect_list:

            expect_list.append(x)


    return expect_list


def run_app():

    user_input = input("请在此输入一连串的数字中间以逗号隔开: \n")

    user_list = [x.strip() for x in user_input.strip().split(',')]

    result = remove_dup_keep_order(user_list)

    print(result)


run_app()

