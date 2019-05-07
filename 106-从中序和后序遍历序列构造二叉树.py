# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 从中序和后序遍历序列构造二叉树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        if len(inorder) != len(postorder):
            return False
        # 根节点是后序遍历最后一个值
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx + 1:], postorder[idx:-1])
        return root
