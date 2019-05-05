# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 删除链表的倒数第k个节点
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 定义链表数据结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 保证给定的k是有效的，仅使用一趟扫描实现
def removeNthFromEnd(head, k):
    dummy = ListNode(-1)
    dummy.next = head
    fast = slow = dummy
    while k and fast:
        fast = fast.next
        k -= 1
    while slow.next and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

# 建立链表
def buildLinkedList():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node6.next = node7
    node5.next = node6
    node4.next = node5
    node3.next = node4
    node2.next = node3
    node1.next = node2
    return node1

# 打印链表
def printLinkedList(head):
    p = head
    ans = []
    while p:
        ans.append(p.val)
        p = p.next
    print(ans)

if __name__ == "__main__":
    k = 3
    head = buildLinkedList()
    printLinkedList(head)
    print("删除倒数第k个节点")
    head = removeNthFromEnd(head,k)
    printLinkedList(head)
