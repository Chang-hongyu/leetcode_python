# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二叉树的层次遍历II
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


# 给定一个二叉树，返回其节点值自底向上的层次遍历

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, ans, root, level):
        if root:
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            self.dfs(ans, root.left, level + 1)
            self.dfs(ans, root.right, level + 1)

    def levelOrderBottom(self, root):
        ans = []
        self.dfs(ans, root, 0)
        return ans[::-1]
