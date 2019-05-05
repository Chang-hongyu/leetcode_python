# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: k个一组翻转链表
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 认为没有额外的头结点
        # 将链表反转k个节点
        def Reverse(head):
            if head == None or head.next == None:
                return head
            pre = head
            cur = head.next
            pre.next = None
            while cur != None:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        if head == None or head.next == None or k < 2:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        begin = head
        i = 1
        while begin != None:
            end = begin
            while i < k:
                if end.next != None:
                    end = end.next
                else:
                    return dummy.next
                i += 1
            pNext = end.next
            # 断开链表 方便翻转并拼接
            end.next = None
            pre.next = Reverse(begin)
            begin.next = pNext
            pre = begin
            begin = pNext
            i = 1
        return dummy.next
