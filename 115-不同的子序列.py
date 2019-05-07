# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 不同的子序列
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 给定一个字符串S和一个字符串T，计算在S的子序列中T出现的个数
# 动态规划思想

class Solution:
    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)

        # dp[i][j]表示s[:j]中含有t[:i]的个数
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        # 当i为0时，dp[i][j]值为1
        for j in range(n + 1):
            dp[0][j] = 1
        for i in range(m):
            for j in range(n):
                if s[j] == t[i]:
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabit"
    ans = Solution().numDistinct(s, t)
    print(ans)
