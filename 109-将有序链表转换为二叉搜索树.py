# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        mid = n // 2
        # 递归思想
        root = TreeNode(nums[mid])
        # 递归左子树
        root.left = self.sortedArrayToBST(nums[:mid])
        # 递归右子树
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    def sortedListToBST(self, head):
        nums = []
        p = head
        while p:
            nums.append(p.val)
            p = p.next
        return self.sortedArrayToBST(nums)
