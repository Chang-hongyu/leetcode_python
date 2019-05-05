# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 两两交换链表中的节点
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swapPairs(head):
    dummy = ListNode(-1)
    cur = dummy
    cur.next = head
    while cur.next and cur.next.next:
        n1 = cur.next
        n2 = cur.next.next
        tmp = n2.next
        n1.next = tmp
        n2.next = n1
        cur.next = n2
        cur = n1
    return dummy.next
