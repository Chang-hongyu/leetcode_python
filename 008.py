# -*- coding:utf-8 -*-
# Author:   Chang-hongyu
# Function:
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def myAtoi(self, str: str) -> int:
        new_str = str.strip()
        if not new_str:
            return 0
        sign = 1
        if new_str[0] in ["+", "-"]:
            if new_str[0] == "-":
                sign = -1
            new_str = new_str[1:]
        ans = 0
        for i in new_str:
            if i.isdigit():
                ans = ans * 10 + int(i)
            else:
                break
        ans *= sign
        if ans > 2147483647:
            return 2147483647
        if ans < -2147483648:
            return -2147483648
        return ans


if __name__ == "__main__":
    s = "-333`1313asdkgad"
    ans = Solution().myAtoi(s)
    print(ans)
