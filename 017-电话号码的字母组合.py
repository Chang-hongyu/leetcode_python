# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个仅包含数字2-9的字符串，返回所有它能表示的不同的字母组合
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


def update(strs, s):
    ans = []
    tmp = list(s)
    for i in strs:
        for j in tmp:
            ans.append(i + j)
    return ans


# 注意da和ad表示的是同一个字母组合
def letterCombinations(digits):
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    if len(digits) == 0:
        return []
    for i, num in enumerate(digits):
        if i == 0:
            ans = list(d[num])
        else:
            ans = update(ans, d[num])
    return ans


if __name__ == "__main__":
    digits = '23'
    ans = letterCombinations(digits)
    print(ans)
