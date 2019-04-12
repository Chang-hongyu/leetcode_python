# -*- coding:utf-8 -*-
# Author: Chang-hongyu
# @Function: 最长回文子串 动态规划
# @Version : 1.0"
# @Contact : 582246340@sjtu.edu.cn"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        # 储存最大长度
        max_len = 0
        max_string = ""
        dp = [[0 for i in range(m)] for j in range(m)]
        for j in range(m):
            for i in range(j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            max_string = s[i:j + 1]
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            max_string = s[i:j + 1]
        return max_string


if __name__ == "__main__":
    s = "babadasdgoitqdbadqlwdgasakdsgqywgdadashd"
    ans = Solution().longestPalindrome(s)
    print(ans)
