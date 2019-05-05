# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 合并k个排序链表
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 本题可以使用分治思想来解决，大大优化时间复杂度，后续会更新

# 法1 暴力求解法
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

# lists: List[ListNode]
def mergeKLists(lists):
    ans = []
    for i in lists:
        while i:
            ans.append(i.val)
            i = i.next
    # 直接将所有的值排序
    ans.sort()
    dummy = ListNode(-1)
    p = dummy
    while ans:
        p.next = ListNode(ans.pop(0))
        p = p.next
    return dummy.next