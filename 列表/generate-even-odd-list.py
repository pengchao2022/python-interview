# 输入一连串的数字，然后生成一个偶数列表，一个奇数列表

def generate_even_odd_list(user_list):

    even_list = [x for x in user_list if x % 2 == 0]

    odd_list = [x for x in user_list if x % 2 != 0]

    return even_list, odd_list


def run_app():

    user_input = input("请在此输入一连串的数字中间以逗号隔开: \n")

    user_list = [int(x.strip()) for x in user_input.strip().split(',')]

    even_list, odd_list = generate_even_odd_list(user_list)

    print(f"偶数列表为: {even_list}")

    print(f"奇数列表为: {odd_list}")


if __name__ == "__main__":

    run_app()

    