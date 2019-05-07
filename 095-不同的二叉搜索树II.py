# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个整数n，生成所有由1~n为节点所组成的二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 输出样例 [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]

# 直接构造这样的二叉搜索树是很复杂的，可以考虑递归思想，二叉搜索树的中序遍历是递增的


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        # 边界条件检测
        if n == 0:
            return []
        # 构造包含1~n节点的二叉搜索树，满足中序遍历递增的条件
        return self.generateTreesDFS(1, n)

    def generateTreesDFS(self, left, right):
        """
        :param left: 给定数值的左端点
        :param right: 给定数值的右端点
        :return: 构成的二叉搜索树根节点的集合
        """

        # 设置递归出口，注意返回是一个列表
        if left > right:
            return [None]
        ans = []
        # 递归思想，依次选取每个值作为根节点
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i - 1)
            right_nodes = self.generateTreesDFS(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    ans.append(root)
        return ans


if __name__ == "__main__":
    ans = Solution().generateTrees(3)
    print(ans)
