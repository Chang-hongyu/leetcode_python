# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定n，输出n对括号组成的所有有效括号
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


def recursion(ans, current, left, right):
    if left == 0 and right == 0:
        ans.append(current)
    if left > 0:
        recursion(ans, current + '(', left - 1, right)
    if right > left:
        recursion(ans, current + ')', left, right - 1)


def generateParenthesis(n):
    ans = []
    recursion(ans, "", n, n)
    return ans


if __name__ == "__main__":
    ans = generateParenthesis(3)
    print(ans)
