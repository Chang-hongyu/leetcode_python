# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 二叉树的中序遍历
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 实现中序遍历的递归算法
class Solution_recursion:
    # 遍历执行的函数
    def inorderTraversal(self, root):
        ans = []
        self.inorder_recursion(root, ans)
        return ans

    # 递归辅助函数
    def inorder_recursion(self, root, ans):
        if root:
            self.inorder_recursion(root.left, ans)
            ans.append(root.val)
            self.inorder_recursion(root.right, ans)


# 实现中序遍历的迭代算法
class Solution_iteration:
    # 迭代时中序遍历使用栈，前序遍历使用队列
    def inorderTraversal(self, root):
        ans = []
        self.inorder_iter(root, ans)
        return ans

    def inorder_iter(self, root, ans):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans.append(root.val)
                root = root.right


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
    ans1 = Solution_recursion().inorderTraversal(root)
    print(ans1)

    root2 = buildTree()
    ans2 = Solution_iteration().inorderTraversal(root2)
    print(ans2)
