# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 将有序数组转换为二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树(AVL)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self,nums):
        n = len(nums)
        if n==0:
            return None
        if n==1:
            return TreeNode(nums[0])
        mid=n//2
        # 递归思想
        root = TreeNode(nums[mid])
        # 递归左子树
        root.left = self.sortedArrayToBST(nums[:mid])
        # 递归右子树
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    print(Solution().sortedArrayToBST(nums).val)