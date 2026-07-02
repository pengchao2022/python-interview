# 练习题：从两个给定列表中创建一个新列表，规则是：取第一个列表中的奇数，取第二个列表中的偶数，然后将它们合并成一个新列表。

# 给定输入：

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# 预期输出：[25, 35, 40, 60, 90]

def deal_two_list(num_list_1, num_list_2):

    odd_num_list = [x for x in num_list_1 if x % 2 != 0]

    even_num_list = [x for x in num_list_2 if x % 2 == 0]

    expect_list = odd_num_list + even_num_list

    return expect_list


def run_app():

    user_input_1 = input("请在此输入第一个列表数字中间以逗号隔开: \n")

    user_input_2 = input("请在此输入第二个列表数字之间以逗号隔开: \n")

    num_list_1 = [int(x.strip()) for x in user_input_1.strip().split(',')]

    num_list_2 = [int(x.strip()) for x in user_input_2.strip().split(',')]

    expect_list = deal_two_list(num_list_1, num_list_2)

    print(expect_list)

    return None


run_app()

