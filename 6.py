# -*- coding:utf-8 -*-
# Author:   Chang-hongyu
# Function: 
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        res = ""
        step = 2 * numRows - 2
        n = len(s)
        for i in range(0, n, step):
            res += s[i]
        for j in range(1,numRows-1):
            slow = -j
            fast = j
            while slow < n or fast < n:
                if 0 < slow < n:
                    res += s[slow]
                if fast < n:
                    res += s[fast]
                slow += step
                fast += step
        for k in range(numRows-1, n, step):
            res += s[k]
        return res

if __name__ == "__main__":
    s = "LEETCODEISHIRING"
    n = 4
    ans = Solution().convert(s,n)
    print(ans)