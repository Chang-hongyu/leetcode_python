# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 给定一个二叉树，判断其是否是一个有效的二叉搜索树
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 利用中序遍历思想

class Solution:
    def isValidBST(self, root):
        # 中序遍历同样的思路
        if not root:
            return True
        # 记录填充节点之前的节点，初始化为None
        pre = None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and root.val < pre.val:
                    return False
                # pre在root之前加入到中序遍历序列中
                pre = root
                root = root.right
        return True

# 对于树     4
#       2       6
#     1   3   5    7
# step1: stack=[]  root=4  pre=None
# step2: stack=[4]  root=2  pre=None
# step3: stack=[4,2]  root=1  pre=None
# step4: stack=[4,2,1]  root=None  pre=None
# step5: stack=[4,2]  pre=None  root=1  pre=1 root=None
# step6: stack=[4]  pre=1  root=2  pre=2  root=3
# step7: stack=[4,3]  root=None
# step8: stack=[4]  pre=2  root=3  pre=3  root=None
# step9: stack=[]  pre=3  root=4  pre=4  root=6
# step10: stack=[6]  root=5
# step11: stack=[6,5]  root=None
# step12: stack=[6]  pre=4  root=5  pre=5  root=None
# step13: stack=[]  pre=5  root=6  pre=6  root=7
# step14: stack=[7]  root=None
# step15: stack=[]  pre=6  root=7  pre=7  root=None
# 结束循环
