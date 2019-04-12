# -*- coding:utf-8 -*-
# Author: Chang-hongyu
# @Function: 将链表代表的数相加，链表首部为最小位
# @Version : 1.0"
# @Contact : 582246340@sjtu.edu.cn"


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        p = head
        carry = 0
        while l1 or l2:
            tmp1 = l1.val if l1 else 0
            tmp2 = l2.val if l2 else 0
            tmp = carry + tmp1 + tmp2
            carry = tmp // 10
            p.next = ListNode(tmp % 10)
            p = p.next
            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next
        if carry == 1:
            p.next = ListNode(1)
        return head.next
