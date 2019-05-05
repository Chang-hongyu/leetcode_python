# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: KMP算法思想
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 法1
def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)
    if m == n:
        if haystack == needle:
            return 0
        else:
            return -1
    # i表示匹配字符串的起点
    for i in range(m):
        j = i
        # k表示匹配的字符串的长度
        k = 0
        while j < m and k < n and haystack[j] == needle[k]:
            j += 1
            k += 1
        if k == n:
            return i
    return -1


# 法2 优化的方法：KMP算法
def getNext(p):
    char_p = list(p)
    next = [0 for _ in range(len(char_p))]
    # 初始化，第一个位置的next值为-1
    next[0] = -1
    j = 0
    # k实时变化，记录上一个位置next指向的元素
    k = -1
    while j < len(char_p) - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            if p[j] == p[k]:
                next[j] = next[k]
            else:
                next[j] = k
        else:
            k = next[k]
    return next


def KMP(t, p):
    char_t = list(t)
    char_p = list(p)
    # 主串的位置
    i = 0
    # 模式串的位置
    j = 0
    # 模式串的更新指针位置列表
    next = getNext(p)
    while i < len(char_t) and j < len(char_p):
        # 当j为-1时，要移动的是i，当然j也要归0
        # 当对应位置相等时，i和k都加1，两种情况可以合并处理
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            # 更新j的指针位置
            j = next[j]
    if j == len(char_p):
        return i - j
    else:
        return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(strStr(haystack, needle))
    print(KMP(haystack, needle))
