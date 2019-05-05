# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定两个排序链表 组合成一个排序链表 返回组合后的head
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    p = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return dummy.next
