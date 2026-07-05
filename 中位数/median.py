# 中位数（Median） 是一组数据按照大小顺序排列后，位于中间位置的数。它能把数据分成相等的两部分。

# 计算步骤

# 1 将数据从小到大排序

# 2 判断数据个数 奇数个数据： 取中间的那个数， 偶数个数据： 取中间两个数的平均值

def get_median(nums: list[int]) -> float: # 接收一个 数字列表 返回浮点型 ，注意 int 也是浮点型的一种，子类型

    
    # 排序
    sorted_nums = sorted(nums)

    n = len(sorted_nums)

    # 判断奇偶
    if n % 2 == 1:
        # 奇数
        return sorted_nums[n // 2]  # 列表的长度 整除 2
    
    else:
        # 偶数，取中间两个数的平均值
        left = sorted_nums[n // 2 - 1]

        right = sorted_nums[n // 2]

        return (left + right) / 2
    
def run_app():

    num_str = input("请在此输入一脸串的数字，数字之间以逗号隔开: ")

    num_list = [int(x.strip()) for x in num_str.strip().split(',')]

    median = get_median(num_list)

    print(f"median is: {median}")


if __name__ == "__main__":

    run_app()

    

    



