# 输入一个整型列表，然后去掉重复的元素 要求保持原有的顺序

def remove_dup_keep_order(nums):

    unique_nums = []

    for num in nums:

        if num not in unique_nums:

            unique_nums.append(num)
    
    return unique_nums


def run_app():

    user_input = input("请在此输入一连串的数字，数字之间以逗号隔开:\n")

    nums = [int(x.strip()) for x in user_input.strip().split(",")]

    expect_nums = remove_dup_keep_order(nums)

    print(expect_nums)


if __name__ == "__main__":

    run_app()

    