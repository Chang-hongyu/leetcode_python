# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def addBinary(self, a, b):
        ans = ""
        m, n, carry = len(a) - 1, len(b) - 1, 0
        while m >= 0 or n >= 0 or carry == 1:
            carry += int(a[m]) if m >= 0 else 0
            carry += int(b[n]) if n >= 0 else 0
            ans = str(carry % 2) + ans
            carry = carry // 2
            m -= 1
            n -= 1
        return ans


if __name__ == "__main__":
    a = '11'
    b = '1'
    ans = Solution().addBinary(a, b)
    print(ans)
