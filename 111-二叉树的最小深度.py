# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 求二叉树的最小深度
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 注意是到根节点的最小距离，当只有根节点时，只能考虑另一条路径
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return 1 + self.minDepth(root.right)
        if root.right == None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
