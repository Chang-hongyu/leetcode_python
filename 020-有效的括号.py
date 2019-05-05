# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定括号字符串 判断是否是一个有效的括号
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


def isValid(s):
    # 使用列表模拟进栈出栈
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and ((stack[-2] == '[' and stack[-1] == ']') or (stack[-2] == '(' and stack[-1] == ')') or (
                stack[-2] == '{' and stack[-1] == '}')):
            stack.pop()
            stack.pop()
    return not stack


if __name__ == "__main__":
    s = "((()))(){([])}"
    ans = isValid(s)
    print(ans)