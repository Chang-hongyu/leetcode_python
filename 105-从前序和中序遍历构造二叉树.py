# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 从前序和中序遍历构造二叉树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        if len(preorder) != len(inorder):
            return False
        # 根节点是前序遍历第一个值
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root
