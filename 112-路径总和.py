# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 路径总和
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if root.left == None and root.right == None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
