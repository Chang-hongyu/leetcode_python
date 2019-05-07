# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 判断两颗二叉树是否相同
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
