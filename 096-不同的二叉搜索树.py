# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 不同的二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 给定一个整数n，求以1~n为节点组成的二叉搜索树有多少种
# 本题可以使用094题的做法，也可以使用卡特兰数的定义直接做


class Solution:
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        # 将dp数组的长度补齐到n+1
        dp += [0 for _ in range(n - 2)]
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


if __name__ == "__main__":
    ans = Solution().numTrees(3)
    print(ans)
