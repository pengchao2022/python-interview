# two sum

# leetcode 第一题 两数字相加

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# 接收用户输入类

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]: # 返回一个 整型列表

        for i in range(len(nums)): # 外循环 i 是索引

            for j in range(i + 1, len(nums)): # j 是列表中紧挨着 i 后面的元素 内循环 j 也是索引

                if nums[i] + nums[j] == target: # 列表使用索引访问

                    return [i, j]               # 返回列表中元素的索引号
                


# 定义Input 类
class UserInput:

    # 方法一 准备输入nums 数组 或者 列表
    def get_array(self) -> list[int]:

        while True:

            try:

                nums_str = input("请在此输入数组， 数字之间以逗号隔开， 如： 2, 7, 11, 15\n")

                nums = [int(x.strip()) for x in nums_str.strip().split(',')] # 列表推导式

                if len(nums) < 2:

                    print("至少要有2 个元素")

                    continue

                return nums
            
            except ValueError:

                print("请输入整数数字之间以逗号隔开")


    # 方法二 准备目标数字 target 
    def get_target(self) -> int:   # 返回 整型

        while True:

            try:
                target = int(input("请在此输入你的目标数字: \n"))

                return target
            
            except ValueError:

                print("请输入有效的整数")


    # 方法三 准备 solution 类的 传递参数
    def get_input_pair(self) -> tuple[list[int], int]: # 返回一个元组 ， 元组里面是整数列表和整型

        nums = self.get_array()
        target = self.get_target()

        return nums, target
    

if __name__ == "__main__":

    # 创建实例对象
    solution = Solution()

    input_data = UserInput()

    # 调用方法
    nums, target = input_data.get_input_pair()

    result = solution.twoSum(nums, target)

    print(f"输入列表: {nums},目标: {target} ")

    print(f"输出: {result}")






