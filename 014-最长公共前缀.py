# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 求给定字符串列表中所有字符串的最长公共前缀
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def longestCommonPrefix(strs):
    ans = ""
    if not strs:
        return ans

    # 记录所有字符串的最短长度，减少后续的计算量
    minlength = float('inf')

    for i in range(len(strs)):
        minlength = min(minlength, len(strs[i]))
    for j in range(minlength):
        for k in range(len(strs)):
            if strs[k][j] != strs[0][j]:
                return ans
        ans += strs[0][j]
    return ans


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    ans = longestCommonPrefix(strs)
    print(ans)
