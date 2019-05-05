# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 平衡二叉树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 注意 平衡二叉树和平衡二叉查找树(AVL)有差别，但二者相同点 都是每个节点的左右子树的高度最多相差1

# 定义一个二叉树节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 递归思想 计算树的高度
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    # 判断树是否为平衡二叉树
    def isBalanced(self, root):
        # 若根节点不存在，则返回True
        if root == None:
            return True
        # 根节点存在，判断左右子树的高度差
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        # 左右子树的高度差满足要求，但是左右子节点的左右子树可能不满足，递归进行左右子节点的左右子树的判断
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

def buildTree():
    # 构造一棵二叉树
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    return node1

if __name__ == "__main__":
    root = buildTree()
    isBalanced = Solution().isBalanced(root)
    print(isBalanced)