# -*- coding:utf-8 -*-
# Author:   Chang-hongyu
# Function:
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        tmp = 0
        while num > 0:
            tmp = tmp * 10 + num % 10
            num = num // 10
        res = tmp if x >= 0 else -tmp
        if -2147483648 <= res <= 2147483647:
            return res
        else:
            return 0


if __name__ == "__main__":
    x = 2131289
    ans = Solution().reverse(x)
    print(ans)
