# 输入一个整型列表，请处理重复的数字，并以小到大的顺序排列

# 冒泡排序

def remove_dup(nums):

    unique_nums = []

    for num in nums:

        if num not in unique_nums:

            unique_nums.append(num)

    return unique_nums


def order_nums(nums):

    n = len(nums)

    for i in range(n):

        for j in range(n - i -1):

            if nums[j] > nums[j + 1]:

                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def run_app():

    user_input = input("请在此输入一连串的数字，数字之间以逗号隔开:\n")

    nums = [int(x.strip()) for x in user_input.strip().split(',')]

    unique_nums = remove_dup(nums)

    order_num_new = order_nums(unique_nums)

    print(order_num_new)


if __name__ == "__main__":

    run_app()

    

