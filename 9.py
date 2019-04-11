# -*- coding:utf-8 -*-
# Author:   Chang-hongyu
# Function: 
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_str = str(x)
        n = len(new_str)
        for i in range(n//2):
            if new_str[i] == new_str[n-1-i]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    x = 12345654321
    ans = Solution().isPalindrome(x)
    print(ans)