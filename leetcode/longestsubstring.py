# 给定一个字符串 s，找出其中不含重复字符的最长子串的长度。

# 注意 三个 关键： 最长 ， 无重复 ， 而且 要连续 ， 子串要连续，不能中间有 隔着一个元素 

class Solution:

    def longestOfSubstring(self, s: str) -> int: # 输入一个字符串 返回一个 整型 最大长度

        # 定义一个集合来存储
        char_str = set()

        left = 0

        max_length = 0

        for right in range(len(s)):

            while s[right] in char_str:

                char_str.remove(s[left])
                left += 1

            char_str.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length

 