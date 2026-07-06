# 输入一个字符串找到里面最长的回文子串

# 回文是 正着读 和 反着读 都是一样的

class Solution:

    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        
        n = len(s)
        start = 0        # 最长回文的起始索引
        max_len = 1      # 最长回文的长度 至少为 1

        def expand(left: int, right: int) -> tuple:
            """从中心向两边扩展, 返回回文的起始索引和长度"""
            while left >= 0 and right < n and s[left] == s[right]:

                left -= 1
                right += 1

            # 注意 退出循环时 left 和 right 已经越界 不匹配
            # 实际回文范围 [left+1, right-1]
            return left + 1, right - left -1
        
        for i in range(n):
            # 奇数长度回文中心是 s[i]
            left1, len1 = expand(i, i)

            # 偶数长度回文 中心是s[i] 和 s[i + 1] 之间
            left2, len2 = expand(i, i + 1)

            # 更新最长回文
            if len1 > max_len:
                start = left1
                max_len = len1

            if len2 > max_len:
                start = left2
                max_len = len2


        return s[start:start + max_len]
    
class UserInput:
    """用户输入类"""

    def get_string(self) -> str:
        """获取用户输入的字符串"""
        while True:

            s = input("请输入一个字符串 长度至少为 1:").strip()

            if not s:
                print("输入不能为空，请重新输入!")
                continue

            # 检查是否只包含字母和数字
            if not s.isalnum():
                print("请输入字母或者数字，中间不能有标点符号或者空格或者特殊符号")

            return s
        
class Program:
    """程序主类"""

    def run_app(self):
        """运行程序"""
        
        print("=" * 50)
        print("最长回文子串查找器")
        print("=" * 50)
        print("说明：找出字符串中最长的回文子串")
        print("回文：正着读和反着读都一样的字符串")
        print("=" * 50)

        # 创建对象
        solution = Solution()
        user_input = UserInput()

        # 获取用户输入
        s = user_input.get_string()

        # 计算结果
        result = solution.longestPalindrome(s)

        # 输出结果
        print("\n" + "=" * 50)
        print(f"输入字符串: {s}")
        print(f"字符串长度: {len(s)}")
        print(f"最长回文子串: {result}")
        print(f"回文子串长度: {len(result)}")
        print("=" * 50)


if __name__ == "__main__":

    program = Program()
    program.run_app()

    