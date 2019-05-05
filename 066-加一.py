# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class Solution:
    def plusOne(self, digits):
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                carry = (digits[i] + carry + 1) // 10
                digits[i] = (digits[i] + carry + 1) % 10
            else:
                carry = (digits[i] + carry) // 10
                digits[i] = (digits[i] + carry) % 10
        if carry == 1:
            return [1] + digits
        else:
            return digits


if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    print(Solution().plusOne(nums))
