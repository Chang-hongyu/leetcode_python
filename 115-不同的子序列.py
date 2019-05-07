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

        # 以t的长度作为外层循环
        for i in range(m):
            for j in range(n):
                # 对应位置的元素相同 本行上一个加上dp矩阵左上角元素
                if s[j] == t[i]:
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j]
                # 对应位置的元素不同 在本行找上一个
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[-1][-1]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabit"
    s1 = "babgbag"
    t1 = "bag"
    ans = Solution().numDistinct(s1, t1)
    print(ans)
