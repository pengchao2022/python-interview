# two sum

# leetcode 第一题 两数字相加

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]: # 返回一个整型列表

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):   # j 是列表中紧跟着 i 的数

                if nums[i] + nums[j] == target:

                    return [i, j]
                
