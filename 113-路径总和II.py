# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 路径总和II
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def path(self, ans, root, sum, subans):
        if root == None:
            return
        if not root.left and not root.right and root.val == sum:
            ans.append(subans + [root.val])
        if root.left:
            self.path(ans, root.left, sum - root.val, subans + [root.val])
        if root.right:
            self.path(ans, root.right, sum - root.val, subans + [root.val])

    def pathSum(self, root, sum):
        ans = []
        self.path(ans, root, sum, [])
        return ans
