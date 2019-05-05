# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定罗马数字字符串 转换为整数
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

def romanToInt(s):
    query = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    for i in range(len(s) - 1):
        if query[s[i]] < query[s[i + 1]]:
            ans -= query[s[i]]
        else:
            ans += query[s[i]]
    ans += query[s[len(s) - 1]]
    return ans


if __name__ == "__main__":
    s = "MCMXCIV"
    ans = romanToInt(s)
    print(ans)
