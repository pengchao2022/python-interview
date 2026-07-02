# 练习目的：这个练习帮助你理解“聚合函数”。虽然 Python 提供了内置函数来直接完成这个任务，但理解如何手动找出极值对于数据归一化非常重要——在处理数据集之前，你通常需要先确定数据的范围。

# 给定输入：nums = [45, 2, 89, 12, 7]

# 预期输出：Largest: 89 Smallest: 2

def fin_min_max(num_list):

    if not num_list:

        return None, None
    
    smallest = num_list[0]
    largest = num_list[0]

    for num in num_list:

        if num > largest:

            largest = num

        if num < smallest:

            smallest = num

    return smallest, largest


def run_app():

    user_input = input("请在此输入一连串数字，数字之间以逗号隔开: \n")

    num_list = [int(x.strip()) for x in user_input.strip().split(',')]

    smallest, largest = fin_min_max(num_list)

    print(f"Smallest is: {smallest}")

    print(f"Largest is: {largest}")


run_app()

