# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二叉树的最大深度
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
