# 输入一个数字，打印出1 到这个数字的 平方 字典

def generate_square_dict(number):

    square_dict = {}

    for i in range(1, number + 1):

        square_dict[i] = i ** 2

    return square_dict


def run_app():

    number = int(input("请在此输入您的数字: \n").strip())

    expect_dict = generate_square_dict(number)

    print(expect_dict)


if __name__ == "__main__":

    run_app()

    