# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 检查二叉树是否是镜像对称
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 辅助函数 判断两颗树是否为镜像
    def solve(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val == q.val:
            return self.solve(p.left, q.right) and self.solve(p.right, q.left)
        return False

    def isSymmetric(self, root):
        if not root:
            return True
        return self.solve(root.left, root.right)
