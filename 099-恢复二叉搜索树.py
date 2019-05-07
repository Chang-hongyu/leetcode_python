# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 恢复二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 二叉搜索树中的两个节点被错误地交换。在不改变其结构的情况下，恢复这棵树。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # 线性空间复杂度
        # 存储树节点的值
        treeVal = []
        # 存储树的节点
        treePointer = []
        # 中序遍历
        self.inorder(root, treeVal, treePointer)
        treeVal.sort()
        for i in range(len(treeVal)):
            treePointer[i].val = treeVal[i]

    def inorder(self, root, treeVal, treePointer):
        # 关键的遍历开始条件
        if root:
            self.inorder(root.left, treeVal, treePointer)
            treeVal.append(root.val)
            treePointer.append(root)
            self.inorder(root.right, treeVal, treePointer)
