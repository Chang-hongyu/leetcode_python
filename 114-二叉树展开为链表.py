# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二叉树展开为链表
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 递归思想
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 不返回任何值，原址修改
    def flatten(self, root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        # 记录之前的右子节点
        tmp = root.right
        root.right = root.left
        # 至关重要的一步
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
