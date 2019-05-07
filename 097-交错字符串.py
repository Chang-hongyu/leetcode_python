# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定三个字符串，验证s3是否是由s1和s2交错组成的
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 动态规划思想
class Solution:
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        p = len(s3)
        if m + n != p:
            return False
        # dp[i][j]表示s1[:i]和s2[:j]是否和s3[:i+j-1]相匹配
        dp = [[False for i in range(n + 1)] for j in range(m + 1)]
        # 都无字符时初始化为True
        dp[0][0] = True
        # 边界条件，列数为0时检测
        for i in range(1, m + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
            else:
                break
        # 边界条件 行数为0时检测
        for j in range(1, n + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] == dp[0][j - 1]
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    ans = Solution().isInterleave(s1, s2, s3)
    print(ans)
