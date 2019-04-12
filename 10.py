# -*- coding:utf-8 -*-
# Author:   Chang-hongyu
# Function:
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False for j in range(n)] for i in range(m)]
        dp[0][0] = True
        for i in range(2, n):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for j in range(1, m):
            for k in range(1, n):
                if s[j - 1] == p[k - 1] or p[k - 1] == ".":
                    dp[j][k] = dp[j - 1][k - 1]
                if p[k - 1] == "*":
                    # 指前面的字符出现的次数
                    dp[j][k] = dp[j][k -
                                     1] or dp[j][k -
                                                 2] or (dp[j -
                                                           1][k] and (s[j -
                                                                        1] == p[k -
                                                                                2] or p[k -
                                                                                        2] == '.'))
        return dp[-1][-1]


if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    ans = Solution().isMatch(s, p)
    print(ans)
