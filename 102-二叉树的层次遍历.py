# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二叉树的层次遍历
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 输出样例
# [
#  [3],
#  [9,20],
#  [15,7]
# ]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, ans, root, level):
        """

        :param ans: 遍历结果
        :param root: 根节点
        :param level: 记录当前遍历层数
        :return:
        """
        if root:
            # 若结果个数少于level+1，加入空列表记录当前层的结果
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            self.dfs(root.left, level + 1)
            self.dfs(root.right, level + 1)

    def levelOrder(self, root):
        ans = []
        self.dfs(ans, root, 0)
        return ans
