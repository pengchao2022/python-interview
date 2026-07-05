# 给定一个字符串 s，找出其中不含重复字符的最长子串的长度。

# 注意 三个 关键： 最长 ， 无重复 ， 而且 要连续 ， 子串要连续，不能中间有 隔着一个元素 


class Solution:

    def longestOfSubString(self, s: str) -> int: # 输入一个字符串，返回最大长度 整型

        # 定义一个空集合存储
        char_set = set()

        left = 0

        max_length = 0

        for right in range(len(s)):

            while s[right] in char_set:

                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length
    

# 定义一个用户输入类
class UserInput:

    def get_string(self) -> str:

        while True:

            try:
                s = input("请在此输入您的字符串:\n").strip()

                if len(s) == 0:

                    print("请输入至少一个字符")

                    continue
                
                return s

            except ValueError:
                print("请输入有效的字符串")

            
if __name__ == "__main__":

    solution = Solution()

    input_str = UserInput()

    s = input_str.get_string()

    result = solution.longestOfSubString(s)

    print(f"输入: {s}")
    print(f"输出: {result}")





        

    
